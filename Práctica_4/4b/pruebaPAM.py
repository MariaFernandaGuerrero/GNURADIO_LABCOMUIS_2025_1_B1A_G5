#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: pruebaPAM
# GNU Radio version: v3.10.11.0-89-ga17f69e7

from PyQt5 import Qt
from gnuradio import qtgui
import os
import sys
import logging as log

def get_state_directory() -> str:
    oldpath = os.path.expanduser("~/.grc_gnuradio")
    try:
        from gnuradio.gr import paths
        newpath = paths.persistent()
        if os.path.exists(newpath):
            return newpath
        if os.path.exists(oldpath):
            log.warning(f"Found persistent state path '{newpath}', but file does not exist. " +
                     f"Old default persistent state path '{oldpath}' exists; using that. " +
                     "Please consider moving state to new location.")
            return oldpath
        # Default to the correct path if both are configured.
        # neither old, nor new path exist: create new path, return that
        os.makedirs(newpath, exist_ok=True)
        return newpath
    except (ImportError, NameError):
        log.warning("Could not retrieve GNU Radio persistent state directory from GNU Radio. " +
                 "Trying defaults.")
        xdgstate = os.getenv("XDG_STATE_HOME", os.path.expanduser("~/.local/state"))
        xdgcand = os.path.join(xdgstate, "gnuradio")
        if os.path.exists(xdgcand):
            return xdgcand
        if os.path.exists(oldpath):
            log.warning(f"Using legacy state path '{oldpath}'. Please consider moving state " +
                     f"files to '{xdgcand}'.")
            return oldpath
        # neither old, nor new path exist: create new path, return that
        os.makedirs(xdgcand, exist_ok=True)
        return xdgcand

sys.path.append(os.environ.get('GRC_HIER_PATH', get_state_directory()))

from PyQt5 import QtCore
from gnuradio import analog
from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from moduladorPAMV2 import moduladorPAMV2  # grc-generated hier_block
import sip
import threading



class pruebaPAM(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "pruebaPAM", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("pruebaPAM")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except BaseException as exc:
            print(f"Qt GUI: Could not set Icon: {str(exc)}", file=sys.stderr)
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("gnuradio/flowgraphs", "pruebaPAM")

        try:
            geometry = self.settings.value("geometry")
            if geometry:
                self.restoreGeometry(geometry)
        except BaseException as exc:
            print(f"Qt GUI: Could not restore geometry: {str(exc)}", file=sys.stderr)
        self.flowgraph_started = threading.Event()

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 100000
        self.fs = fs = 1000
        self.fm = fm = 100
        self.D_4 = D_4 = 10
        self.D_3 = D_3 = 10
        self.D_2 = D_2 = 10
        self.D_1 = D_1 = 10
        self.D = D = 10
        self.Am = Am = 1

        ##################################################
        # Blocks
        ##################################################

        self._fs_range = qtgui.Range(0, 10000, 1, 1000, 200)
        self._fs_win = qtgui.RangeWidget(self._fs_range, self.set_fs, "frecuencia impulsos", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._fs_win)
        self._fm_range = qtgui.Range(0, 10000, 10, 100, 200)
        self._fm_win = qtgui.RangeWidget(self._fm_range, self.set_fm, "freqmensaje", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._fm_win)
        self._D_4_range = qtgui.Range(0, 50, 1, 10, 200)
        self._D_4_win = qtgui.RangeWidget(self._D_4_range, self.set_D_4, "retardosonido", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._D_4_win)
        self._D_3_range = qtgui.Range(0, 50, 1, 10, 200)
        self._D_3_win = qtgui.RangeWidget(self._D_3_range, self.set_D_3, "retardo3", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._D_3_win)
        self._D_2_range = qtgui.Range(0, 50, 1, 10, 200)
        self._D_2_win = qtgui.RangeWidget(self._D_2_range, self.set_D_2, "retardo2", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._D_2_win)
        self._D_1_range = qtgui.Range(0, 50, 1, 10, 200)
        self._D_1_win = qtgui.RangeWidget(self._D_1_range, self.set_D_1, "retardo1", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._D_1_win)
        self._D_range = qtgui.Range(0, 50, 1, 10, 200)
        self._D_win = qtgui.RangeWidget(self._D_range, self.set_D, "ancho impulsos", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._D_win)
        self._Am_range = qtgui.Range(0, 10, 0.1, 1, 200)
        self._Am_win = qtgui.RangeWidget(self._Am_range, self.set_Am, "amplitudmpulsos", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._Am_win)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
            1024, #size
            samp_rate, #samp_rate
            "", #name
            5, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(5):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self.moduladorPAMV2_0_2_0 = moduladorPAMV2(
            D=D,
            fs=fs,
            samp_rate=samp_rate,
        )
        self.moduladorPAMV2_0_2 = moduladorPAMV2(
            D=D,
            fs=fs,
            samp_rate=samp_rate,
        )
        self.moduladorPAMV2_0_1 = moduladorPAMV2(
            D=D,
            fs=fs,
            samp_rate=samp_rate,
        )
        self.moduladorPAMV2_0_0 = moduladorPAMV2(
            D=D,
            fs=fs,
            samp_rate=samp_rate,
        )
        self.moduladorPAMV2_0 = moduladorPAMV2(
            D=D,
            fs=fs,
            samp_rate=samp_rate,
        )
        self.blocks_wavfile_source_0 = blocks.wavfile_source('file_example_WAV_1MG.wav', True)
        self.blocks_delay_0_2_0 = blocks.delay(gr.sizeof_float*1, D_4)
        self.blocks_delay_0_2 = blocks.delay(gr.sizeof_float*1, D_3)
        self.blocks_delay_0_1 = blocks.delay(gr.sizeof_float*1, D_2)
        self.blocks_delay_0_0 = blocks.delay(gr.sizeof_float*1, D_1)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.analog_sig_source_x_0_2 = analog.sig_source_f(samp_rate, analog.GR_SAW_WAVE, fm, Am, 0, 0)
        self.analog_sig_source_x_0_1 = analog.sig_source_f(samp_rate, analog.GR_SAW_WAVE, fm, Am, 0, 0)
        self.analog_sig_source_x_0_0 = analog.sig_source_f(samp_rate, analog.GR_SAW_WAVE, fm, Am, 0, 0)
        self.analog_sig_source_x_0 = analog.sig_source_f(samp_rate, analog.GR_SAW_WAVE, fm, Am, 0, 0)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.moduladorPAMV2_0, 0))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.moduladorPAMV2_0_0, 0))
        self.connect((self.analog_sig_source_x_0_1, 0), (self.moduladorPAMV2_0_1, 0))
        self.connect((self.analog_sig_source_x_0_2, 0), (self.moduladorPAMV2_0_2, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.qtgui_time_sink_x_0, 4))
        self.connect((self.blocks_delay_0_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_delay_0_0, 0), (self.qtgui_time_sink_x_0, 1))
        self.connect((self.blocks_delay_0_1, 0), (self.blocks_add_xx_0, 2))
        self.connect((self.blocks_delay_0_1, 0), (self.qtgui_time_sink_x_0, 2))
        self.connect((self.blocks_delay_0_2, 0), (self.blocks_add_xx_0, 3))
        self.connect((self.blocks_delay_0_2, 0), (self.qtgui_time_sink_x_0, 3))
        self.connect((self.blocks_delay_0_2_0, 0), (self.blocks_add_xx_0, 4))
        self.connect((self.blocks_wavfile_source_0, 0), (self.moduladorPAMV2_0_2_0, 0))
        self.connect((self.moduladorPAMV2_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.moduladorPAMV2_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.moduladorPAMV2_0_0, 0), (self.blocks_delay_0_0, 0))
        self.connect((self.moduladorPAMV2_0_1, 0), (self.blocks_delay_0_1, 0))
        self.connect((self.moduladorPAMV2_0_2, 0), (self.blocks_delay_0_2, 0))
        self.connect((self.moduladorPAMV2_0_2_0, 0), (self.blocks_delay_0_2_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("gnuradio/flowgraphs", "pruebaPAM")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_1.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_2.set_sampling_freq(self.samp_rate)
        self.moduladorPAMV2_0.set_samp_rate(self.samp_rate)
        self.moduladorPAMV2_0_0.set_samp_rate(self.samp_rate)
        self.moduladorPAMV2_0_1.set_samp_rate(self.samp_rate)
        self.moduladorPAMV2_0_2.set_samp_rate(self.samp_rate)
        self.moduladorPAMV2_0_2_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)

    def get_fs(self):
        return self.fs

    def set_fs(self, fs):
        self.fs = fs
        self.moduladorPAMV2_0.set_fs(self.fs)
        self.moduladorPAMV2_0_0.set_fs(self.fs)
        self.moduladorPAMV2_0_1.set_fs(self.fs)
        self.moduladorPAMV2_0_2.set_fs(self.fs)
        self.moduladorPAMV2_0_2_0.set_fs(self.fs)

    def get_fm(self):
        return self.fm

    def set_fm(self, fm):
        self.fm = fm
        self.analog_sig_source_x_0.set_frequency(self.fm)
        self.analog_sig_source_x_0_0.set_frequency(self.fm)
        self.analog_sig_source_x_0_1.set_frequency(self.fm)
        self.analog_sig_source_x_0_2.set_frequency(self.fm)

    def get_D_4(self):
        return self.D_4

    def set_D_4(self, D_4):
        self.D_4 = D_4
        self.blocks_delay_0_2_0.set_dly(int(self.D_4))

    def get_D_3(self):
        return self.D_3

    def set_D_3(self, D_3):
        self.D_3 = D_3
        self.blocks_delay_0_2.set_dly(int(self.D_3))

    def get_D_2(self):
        return self.D_2

    def set_D_2(self, D_2):
        self.D_2 = D_2
        self.blocks_delay_0_1.set_dly(int(self.D_2))

    def get_D_1(self):
        return self.D_1

    def set_D_1(self, D_1):
        self.D_1 = D_1
        self.blocks_delay_0_0.set_dly(int(self.D_1))

    def get_D(self):
        return self.D

    def set_D(self, D):
        self.D = D
        self.moduladorPAMV2_0.set_D(self.D)
        self.moduladorPAMV2_0_0.set_D(self.D)
        self.moduladorPAMV2_0_1.set_D(self.D)
        self.moduladorPAMV2_0_2.set_D(self.D)
        self.moduladorPAMV2_0_2_0.set_D(self.D)

    def get_Am(self):
        return self.Am

    def set_Am(self, Am):
        self.Am = Am
        self.analog_sig_source_x_0.set_amplitude(self.Am)
        self.analog_sig_source_x_0_0.set_amplitude(self.Am)
        self.analog_sig_source_x_0_1.set_amplitude(self.Am)
        self.analog_sig_source_x_0_2.set_amplitude(self.Am)




def main(top_block_cls=pruebaPAM, options=None):

    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()
    tb.flowgraph_started.set()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
