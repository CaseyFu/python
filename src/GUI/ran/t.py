# - * - coding:utf-8-*-
import wx
import wx.xrc
import wx.dataview
import os
import csv
from _datetime import datetime

cmd = os.path.realpath('./Zbar/bin/zbarimg.exe')
csvdata = []


class MyFramel (wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"条形码识别程序",
                          pos=wx.DefaultPosition, size=wx.Size(886, 302),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        bSizer5 = wx.BoxSizer(wx.VERTICAL)
        self.m_toolBar2 = wx.ToolBar(self, wx.ID_ANY, wx.DefaultPosition,
                                     wx.DefaultSize, wx.TB_HORIZONTAL)
        self.m_open = self.m_toolBar2.AddTool(wx.ID_ANY, u"打开",
                                              wx.ArtProvider.GetBitmap(
                                                  wx.ART_FILE_OPEN, wx.ART_TOOLBAR),
                                              wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None)
        self.m_export = self.m_toolBar2.AddTool(wx.ID_ANY, u"导出",
                                                wx.ArtProvider.GetBitmap(
                                                    wx.ART_FILE_SAVE, wx.ART_TOOLBAR),
                                                wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString,
                                                wx.EmptyString, None)
        self.m_toolBar2.Realize()
        bSizer5.Add(self.m_toolBar2, 0, wx.EXPAND, 5)
        gSizer1 = wx.GridSizer(1, 2, 0, 0)
        self.m_dvc = wx.dataview.DataViewListCtrl(self, wx.ID_ANY,
                                                  wx.DefaultPosition, wx.DefaultSize,
                                                  wx.dataview.DV_MULTIPLE | wx.dataview.DV_ROW_LINES)
        gSizer1.Add(self.m_dvc, 0, wx.EXPAND, 5)
        self.m_out = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString,
                                 wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE)
        gSizer1.Add(self.m_out, 0, wx.EXPAND, 5)
        bSizer5.Add(gSizer1, 1, wx.EXPAND, 5)
        self.SetSizer(bSizer5)
        self.Layout()
        self.Centre(wx.BOTH)
        # Connect Events
        self.Bind(wx.EVT_TOOL, self.openimgs, id=self.m_open.GetId())
        self.Bind(wx.EVT_TOOL, self.export2csv, id=self.m_export.GetId())
        # Mycode
        self.m_dvc.AppendTextColumn(u'日期')
        self.m_dvc.AppendTextColumn(u'条形码', width=120)
        self.m_dvc.AppendTextColumn(u'文件夹地址', width=400)

        def __del__(self):
            pass

    def openimgs(self, event):
        dlg = wx.FileDialog(
            self, message="Choose some images",
            defaultDir=os.getcwd(),
            defaultFile="",
            wildcard=wildcard,
            style=wx.FD_OPEN | wx.FD_MULTIPLE | wx.FD_CHANGE_DIR
        )
        if dlg.ShowModal() == wx.ID_OK:
            self.m_out.WriteText('Recognizing!\n')
            paths = dlg.GetPaths()
            for path in paths:
                tmp = os.popen('%s %s' % (cmd, path)).readlines()
                barNum = ''
                i = 0
                while barNum == '' and i < len(tmp):
                    barNum = tmp[i].strip()
                    i += 1
                if barNum == '':
                    self.m_out.WriteText('%s recognize fails!\n' % path)
                    continue
                newname = ('%s\\%s%s' % (os.path.dirname(
                    path), barNum, os.path.splitext(path)[1])).split(":")[2]
                try:
                    os.rename(path, newname)
                    item = [datetime.now().strftime('%Y-%m-%d'),
                            "'%s'" % barNum, newname]
                    self.m_dvc.AppendItem(item)
                    csvdata.append(item)
                    self.m_out.WriteText('%s Recognize Done!\n' % barNum)
                except Exception as e:
                    self.m_out.WriteText('%s rename fails!\n' % path)
                    self.m_out.WriteText(str(e))
        dlg.Destroy()

    def export2csv(self, event):
        dlg = wx.FileDialog(
            self, message="Save file as...", defaultDir=os.getcwd(),
            defaultFile='', wildcard=wildcard2, style=wx.FD_SAVE
        )
        dlg.SetFilterIndex(2)
        if dlg.ShowModal() == wx.ID_OK:
            self.m_out.WriteText('Exporting!\n')
            path = dlg.GetPath()
            try:
                with open(path, 'ab')as csbfile:
                    writer = csv.writer(
                        csvfile, dialect='excel', quoting=csv.QUOTR_ALL)
                    for row in csvdata:
                        writer.writerow(row)
                self.m_out.WriteText('%s Export Done!\n!' % path)
            except Exception as e:
                self.m_out.WriteText(str(e))
        dlg.Destroy()


wildcard = "Pictures(*.jpg,*.png)|.jpg;*.png|All files(*.*)|*.*"
wildcard2 = "CSV files(*.csv)|*.csv"


app = wx.App()
win = MyFramel(None)
win.Show()
app.MainLoop()
