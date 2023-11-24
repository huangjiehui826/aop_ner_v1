# -*-coding:utf-8-*-
import os
import csv
import pickle
from nltk import sent_tokenize
from time import time
import numpy as np
import nltk
import re
from nltk.stem import WordNetLemmatizer
import requests
import json
import requests
from fake_useragent import UserAgent
from lxml.html import etree
from time import time
import pandas as pd
import fnmatch
import warnings
import fitz
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
                           QCursor, QFont, QFontDatabase, QGradient,
                           QIcon, QImage, QKeySequence, QLinearGradient,
                           QPainter, QPalette, QPixmap, QRadialGradient,
                           QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
                               QHBoxLayout, QLabel, QLineEdit, QMainWindow,
                               QMenu, QMenuBar, QPushButton, QSizePolicy,
                               QSpacerItem, QStatusBar, QTextEdit, QVBoxLayout,
                               QWidget)
warnings.filterwarnings("ignore", category=UserWarning)
wordnet_lematizer = WordNetLemmatizer()

characters = [' ', '.', 'DBSCAN', ':', ';', '?', '[', ']', '&', '!', '*', '@', '#', '$', '%', '...', '^', '{', '}']
requests.packages.urllib3.disable_warnings()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(565, 398)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 10, 566, 420))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.horizontalLayout_3.addItem(self.verticalSpacer_3)

        self.software_name = QLabel(self.layoutWidget)
        self.software_name.setObjectName(u"software_name")
        font = QFont()
        font.setFamilies([u"\u5b8b\u4f53"])
        font.setPointSize(20)
        font.setBold(True)
        self.software_name.setFont(font)
        self.software_name.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.software_name)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)


        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.input_dict_label = QLabel(self.layoutWidget)
        self.input_dict_label.setObjectName(u"input_dict_label")
        font1 = QFont()
        font1.setFamilies([u"\u5b8b\u4f53"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.input_dict_label.setFont(font1)

        self.horizontalLayout.addWidget(self.input_dict_label)

        self.input_dict_name = QLineEdit(self.layoutWidget)
        self.input_dict_name.setObjectName(u"input_dict_name")

        self.horizontalLayout.addWidget(self.input_dict_name)

        self.clean_dict_name = QPushButton(self.layoutWidget)
        self.clean_dict_name.setObjectName(u"clean_dict_name")
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        self.clean_dict_name.setFont(font2)

        self.horizontalLayout.addWidget(self.clean_dict_name)

        self.new_dict = QPushButton(self.layoutWidget)
        self.new_dict.setObjectName(u"new_dict")
        self.new_dict.setFont(font1)

        self.horizontalLayout.addWidget(self.new_dict)

        self.aop_crawler = QPushButton(self.layoutWidget)
        self.aop_crawler.setObjectName(u"aop_crawler")
        self.aop_crawler.setFont(font1)

        self.horizontalLayout.addWidget(self.aop_crawler)


        self.gridLayout.addLayout(self.horizontalLayout, 3, 1, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.process_label = QLabel(self.layoutWidget)
        self.process_label.setObjectName(u"process_label")
        self.process_label.setFont(font1)

        self.horizontalLayout_4.addWidget(self.process_label)

        self.output_text = QTextEdit(self.layoutWidget)
        self.output_text.setObjectName(u"output_text")
        font3 = QFont()
        font3.setFamilies([u"\u5b8b\u4f53"])
        self.output_text.setFont(font3)

        self.horizontalLayout_4.addWidget(self.output_text)

        self.clean_output_process = QPushButton(self.layoutWidget)
        self.clean_output_process.setObjectName(u"clean_output_process")
        self.clean_output_process.setFont(font2)

        self.horizontalLayout_4.addWidget(self.clean_output_process)


        self.gridLayout.addLayout(self.horizontalLayout_4, 4, 0, 1, 2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.input_type_label = QLabel(self.layoutWidget)
        self.input_type_label.setObjectName(u"input_type_label")
        self.input_type_label.setFont(font1)

        self.horizontalLayout_2.addWidget(self.input_type_label)

        self.input_type = QComboBox(self.layoutWidget)
        self.input_type.addItem("")
        self.input_type.addItem("")
        self.input_type.addItem("")
        self.input_type.addItem("")
        self.input_type.setObjectName(u"input_type")
        font4 = QFont()
        font4.setFamilies([u"\u5b8b\u4f53"])
        font4.setPointSize(10)
        font4.setBold(True)
        self.input_type.setFont(font4)

        self.horizontalLayout_2.addWidget(self.input_type)

        self.input_text_path = QLabel(self.layoutWidget)
        self.input_text_path.setObjectName(u"input_text_path")
        self.input_text_path.setFont(font1)

        self.horizontalLayout_2.addWidget(self.input_text_path)

        self.input_text = QLineEdit(self.layoutWidget)
        self.input_text.setObjectName(u"input_text")

        self.horizontalLayout_2.addWidget(self.input_text)

        self.clean_button_input = QPushButton(self.layoutWidget)
        self.clean_button_input.setObjectName(u"clean_button_input")
        self.clean_button_input.setFont(font2)

        self.horizontalLayout_2.addWidget(self.clean_button_input)


        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.load_dict = QPushButton(self.layoutWidget)
        self.load_dict.setObjectName(u"load_dict")
        self.load_dict.setFont(font1)

        self.horizontalLayout_5.addWidget(self.load_dict)

        self.line_7 = QFrame(self.layoutWidget)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.VLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_5.addWidget(self.line_7)

        self.start_ner = QPushButton(self.layoutWidget)
        self.start_ner.setObjectName(u"start_ner")
        self.start_ner.setFont(font1)

        self.horizontalLayout_5.addWidget(self.start_ner)

        self.line_6 = QFrame(self.layoutWidget)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.VLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_5.addWidget(self.line_6)

        self.ner_output = QPushButton(self.layoutWidget)
        self.ner_output.setObjectName(u"ner_output")
        self.ner_output.setFont(font1)

        self.horizontalLayout_5.addWidget(self.ner_output)


        self.gridLayout.addLayout(self.horizontalLayout_5, 5, 0, 1, 2)


        self.verticalLayout.addLayout(self.gridLayout)

        self.verticalSpacer_4 = QSpacerItem(18, 37, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 565, 22))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.software_name.setText(QCoreApplication.translate("MainWindow", u"\u82f1\u6587\u6587\u732e\u6bd2\u7406\u5b66\u672f\u8bed\u547d\u540d\u5b9e\u4f53\u8bc6\u522b\u7cfb\u7edf", None))
        self.input_dict_label.setText(QCoreApplication.translate("MainWindow", u"\u8f93\u5165\u8bcd\u5178\uff1a", None))
        self.clean_dict_name.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u9664", None))
        self.new_dict.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u6216\u66f4\u65b0\u8bcd\u5178", None))
        self.aop_crawler.setText(QCoreApplication.translate("MainWindow", u"\u66f4\u65b0AOP", None))
        self.process_label.setText(QCoreApplication.translate("MainWindow", u"\u7a0b\u5e8f\u6267\u884c\u60c5\u51b5\uff1a", None))
        self.clean_output_process.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u9664", None))
        self.input_type_label.setText(QCoreApplication.translate("MainWindow", u"\u8f93\u5165\u7c7b\u578b\uff1a", None))
        self.input_type.setItemText(0, QCoreApplication.translate("MainWindow", u"\u6587\u672c", None))
        self.input_type.setItemText(1, QCoreApplication.translate("MainWindow", u"\u8bcd\u5178", None))
        self.input_type.setItemText(2, QCoreApplication.translate("MainWindow", u"\u6587\u4ef6", None))
        self.input_type.setItemText(3, QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u5939", None))

        self.input_text_path.setText(QCoreApplication.translate("MainWindow", u"\u8f93\u5165\u6587\u672c\u6216\u8def\u5f84\uff1a", None))
        self.clean_button_input.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u9664", None))
        self.load_dict.setText(QCoreApplication.translate("MainWindow", u"\u52a0\u8f7d\u8bcd\u5178", None))
        self.start_ner.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u8bc6\u522b", None))
        self.ner_output.setText(QCoreApplication.translate("MainWindow", u"\u8bc6\u522b\u5e76\u8f93\u51fa\u6587\u4ef6", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u5e2e\u52a9", None))


class Spiders(object):
    def __init__(self, url):
        self.url = url

    def get_content_from(self):
        user_agent = UserAgent()
        my_header = {'user-agent': user_agent.random}
        try:
            scode = requests.get(
                self.url, headers=my_header, verify=False, timeout=10
            ).content.decode("utf8", "ignore")
            return scode
        except Exception as e:
            print("Error:{}".format(e))


def delete_characters(token_words):
    words_list = [word for word in token_words if word not in characters]
    words_list = [word.lower() for word in words_list]
    words_list = [x.replace('.', '') for x in words_list]
    words_list = [x.replace('‘', '\'') for x in words_list]
    words_list = [x.replace('：', ':') for x in words_list]
    words_list = [x.replace(';', '') for x in words_list]
    words_list = [x.replace('?', '') for x in words_list]
    words_list = [x.replace('\"', '\'') for x in words_list]
    words_list = [x.replace('&', '') for x in words_list]
    words_list = [x.replace('*', '') for x in words_list]
    words_list = [x.replace('@', '') for x in words_list]
    words_list = [x.replace('!', '') for x in words_list]
    words_list = [x.replace('#', '') for x in words_list]
    words_list = [x.replace('%', '') for x in words_list]
    words_list = [x.replace('^', '') for x in words_list]
    words_list = [x.replace('(', '') for x in words_list]
    words_list = [x.replace(')', '') for x in words_list]
    words_list = [x.replace(',', '') for x in words_list]
    words_list = [wordnet_lematizer.lemmatize(token_word) for token_word in words_list]
    return words_list


def get_pdf_text(filepath):
    """
    输入pdf文件的文件路径，将pdf中的文本抽取出来
    :param filepath: pdf的文件路径
    :return: pdf文件的所有文本
    """
    with fitz.open(filepath) as pdf:
        file_content = ''
        for page in pdf:
            file_content += page.get_text()
            file_content += ' '
    return file_content


def clean_text(content):
    """
    清洗文本中的换行符，并将换行符转换成空格
    :param content: 输入的文本内容
    :return: 将换行符转换为空格后的文本内容
    """
    content = content.strip()
    content = content.replace('\n', ' ')
    return content


class GenerateDict(object):
    def __init__(self, get_filepath, get_dict_name='initial'):
        self.get_filepath = get_filepath
        self.get_dict_name = get_dict_name
        self.current_path = os.getcwd()
        one_aop_list = {}
        prefer_two_aop = {}
        two_aop_list = {}
        prefer_three_aop = {}
        three_aop_list = {}
        prefer_four_aop = {}
        four_aop_list = {}
        two_repeat_one = {}
        three_repeat_one = {}
        four_repeat_one = {}
        positive_trend = {}
        negative_trend = {}
        other_trend = {}
        all_trend = {}
        self.one_aop_list = one_aop_list
        self.prefer_two_aop = prefer_two_aop
        self.two_aop_list = two_aop_list
        self.prefer_three_aop = prefer_three_aop
        self.three_aop_list = three_aop_list
        self.prefer_four_aop = prefer_four_aop
        self.four_aop_list = four_aop_list
        self.two_repeat_one = two_repeat_one
        self.three_repeat_one = three_repeat_one
        self.four_repeat_one = four_repeat_one
        self.positive_trend = positive_trend
        self.negative_trend = negative_trend
        self.other_trend = other_trend
        self.all_trend = all_trend
        self.aop_dict = {}
        self.aop_entity = {}
        self.aop_id_element = {}

    def new_dict(self):
        self.generate_aop_dict()
        folder_name = self.get_dict_name
        dict_filepath = self.current_path + '\\' + folder_name
        aop_entity_save_pat = dict_filepath + '\\' + 'aop_entity' + '.txt'
        with open(aop_entity_save_pat, 'r', encoding='utf-8-sig') as f:
            for rows in f.readlines():
                rows = rows.strip()
                word_split = rows.split()
                if len(word_split) == 1:
                    self.one_aop_list[word_split[0]] = 1
                elif len(word_split) == 2:
                    if word_split[0] not in self.prefer_two_aop:
                        self.prefer_two_aop[word_split[0]] = 1
                    two_word = word_split[0] + ' ' + word_split[1]
                    self.two_aop_list[two_word] = 1
                elif len(word_split) == 3:
                    if word_split[0] not in self.prefer_three_aop:
                        self.prefer_three_aop[word_split[0]] = 1
                    three_word = word_split[0] + ' ' + word_split[1] + ' ' + word_split[2]
                    self.three_aop_list[three_word] = 1
                elif len(word_split) == 4:
                    if word_split[0] not in self.prefer_four_aop:
                        self.prefer_four_aop[word_split[0]] = 1
                    four_word = word_split[0] + ' ' + word_split[1] + ' ' + word_split[2] + ' ' + word_split[3]
                    self.four_aop_list[four_word] = 1
        for word in self.prefer_two_aop:
            if word in self.one_aop_list:
                self.two_repeat_one[word] = 1
        for word in self.prefer_three_aop:
            if word in self.one_aop_list:
                self.three_repeat_one[word] = 1
        for word in self.prefer_four_aop:
            if word in self.one_aop_list:
                self.four_repeat_one[word] = 1
        self.save_file()

    def generate_aop_dict(self):
        folder_name = self.get_dict_name
        dict_filepath = self.current_path + '\\' + folder_name
        tendency_save_pat = dict_filepath + '\\' + 'Tendency' + '.txt'
        positive_trend_save_pat = dict_filepath + '\\' + 'positive_trend' + '.txt'
        negative_trend_save_pat = dict_filepath + '\\' + 'negative_trend' + '.txt'
        other_trend_save_pat = dict_filepath + '\\' + 'other_trend' + '.txt'
        acronym_name_save_pat = dict_filepath + '\\' + 'Acronym_name' + '.txt'
        aop_element_save_pat = dict_filepath + '\\' + 'aop_element' + '.csv'
        with open(tendency_save_pat, 'r', encoding='utf-8-sig') as reader1:
            for line in reader1.readlines():
                line = line.strip()
                self.all_trend[line] = 1
        with open(positive_trend_save_pat, 'r', encoding='utf-8-sig') as reader2:
            for line in reader2.readlines():
                line = line.strip()
                self.positive_trend[line] = 1
        with open(negative_trend_save_pat, 'r', encoding='utf-8-sig') as reader3:
            for line in reader3.readlines():
                line = line.strip()
                self.negative_trend[line] = 1
        with open(other_trend_save_pat, 'r', encoding='utf-8-sig') as reader4:
            for line in reader4.readlines():
                line = line.strip()
                self.other_trend[line] = 1
        acronym_name = {}
        with open(acronym_name_save_pat, 'r', encoding='utf-8-sig') as r:
            for line in r.readlines():
                line = line.strip()
                line_split = re.split(r'\t+', line)
                acronym_name[line_split[0]] = line_split[1]
        with open(aop_element_save_pat, 'r', encoding='utf-8-sig') as f1:
            csv_reader = csv.reader(f1)
            title = 0
            for rows in csv_reader:
                if title != 0:
                    tmp_mark = []
                    replace_acronym_mark = []
                    is_label = rows[10]
                    if is_label == 'Y':
                        aop_id = rows[1]
                        aop_element = rows[0]
                        self.aop_id_element[aop_id] = aop_element
                        aop_sort = rows[2]
                        for mark in rows[4: 9]:
                            if mark:
                                mark = mark.strip()
                                mark_split = mark.split()
                                get_mark = delete_characters(mark_split)
                                if len(get_mark) == 4:
                                    new_mark = get_mark[0] + ' ' + get_mark[1] + ' ' + get_mark[2] + ' ' + get_mark[3]
                                    if new_mark not in self.aop_entity:
                                        self.aop_entity[new_mark] = 1
                                elif len(get_mark) == 3:
                                    new_mark = get_mark[0] + ' ' + get_mark[1] + ' ' + get_mark[2]
                                    if new_mark not in self.aop_entity:
                                        self.aop_entity[new_mark] = 1
                                elif len(get_mark) == 2:
                                    new_mark = get_mark[0] + ' ' + get_mark[1]
                                    if new_mark not in self.aop_entity:
                                        self.aop_entity[new_mark] = 1
                                elif len(get_mark) == 1:
                                    new_mark = get_mark[0]
                                    if new_mark not in self.aop_entity:
                                        self.aop_entity[new_mark] = 1
                                else:
                                    new_mark = mark
                                tmp_mark.append(new_mark)
                                if mark in acronym_name:
                                    replace_acronym_mark.append(acronym_name[mark].lower())
                                else:
                                    replace_acronym_mark.append(new_mark)
                            else:
                                break

                        if aop_id not in self.aop_dict:
                            self.aop_dict[aop_id] = {'mark': [], 'trend': 's', 'sort': aop_sort}
                        if tmp_mark != replace_acronym_mark:
                            self.aop_dict[aop_id]['mark'].append(tmp_mark)
                            self.aop_dict[aop_id]['mark'].append(replace_acronym_mark)
                        else:
                            self.aop_dict[aop_id]['mark'].append(tmp_mark)
                        trend = rows[9].lower().strip()
                        trend_split = trend.split()
                        trend_split = delete_characters(trend_split)
                        if len(trend_split) == 2:
                            trend = trend_split[0] + ' ' + trend_split[1]
                        if trend in acronym_name:
                            trend = acronym_name[trend]
                        if trend not in self.aop_entity:
                            self.aop_entity[trend] = 1
                        if trend in self.positive_trend:
                            self.aop_dict[aop_id]['trend'] = 'p'
                        elif trend in self.negative_trend:
                            self.aop_dict[aop_id]['trend'] = 'n'
                        elif trend in self.other_trend:
                            self.aop_dict[aop_id]['trend'] = trend
                        else:
                            self.aop_dict[aop_id]['trend'] = 's'
                else:
                    title += 1

        dict_filepath = self.current_path + '\\' + self.get_dict_name
        if not os.path.exists(dict_filepath):
            os.makedirs(dict_filepath)
        aop_dict_save_pat = dict_filepath + '\\' + 'aop_dict' + '.pkl'
        aop_entity_save_pat = dict_filepath + '\\' + 'aop_entity' + '.txt'
        aop_id_element_save_pat = dict_filepath + '\\' + 'aop_id_element' + '.pkl'
        with open(aop_dict_save_pat, 'wb') as w:
            pickle.dump(self.aop_dict, w)
        with open(aop_entity_save_pat, 'w', encoding='utf-8-sig') as w1:
            for entity in self.aop_entity:
                w1.write(entity + '\n')
        with open(aop_id_element_save_pat, 'wb') as w:
            pickle.dump(self.aop_id_element, w)

    def save_file(self):
        folder_name = self.get_dict_name
        dict_filepath = self.current_path + '\\' + folder_name
        if not os.path.exists(dict_filepath):
            os.makedirs(dict_filepath)
        one_aop_list_save_path = dict_filepath + '\\' + 'one_aop_list' + '.txt'
        prefer_two_aop_save_path = dict_filepath + '\\' + 'prefer_two_aop' + '.txt'
        two_aop_list_save_pat = dict_filepath + '\\' + 'two_aop_list' + '.txt'
        prefer_three_aop_save_pat = dict_filepath + '\\' + 'prefer_three_aop' + '.txt'
        three_aop_list_save_pat = dict_filepath + '\\' + 'three_aop_list' + '.txt'
        prefer_four_aop_save_pat = dict_filepath + '\\' + 'prefer_four_aop' + '.txt'
        four_aop_list_save_pat = dict_filepath + '\\' + 'four_aop_list' + '.txt'
        two_repeat_one_save_pat = dict_filepath + '\\' + 'two_repeat_one' + '.txt'
        three_repeat_one_save_pat = dict_filepath + '\\' + 'three_repeat_one' + '.txt'
        four_repeat_one_save_pat = dict_filepath + '\\' + 'four_repeat_one' + '.txt'
        with open(one_aop_list_save_path, 'w', encoding='utf-8-sig') as w1:
            for word in self.one_aop_list:
                w1.write(word + '\n')
        with open(prefer_two_aop_save_path, 'w', encoding='utf-8-sig') as w2:
            for word in self.prefer_two_aop:
                w2.write(word + '\n')
        with open(two_aop_list_save_pat, 'w', encoding='utf-8-sig') as w3:
            for word in self.two_aop_list:
                w3.write(word + '\n')
        with open(prefer_three_aop_save_pat, 'w', encoding='utf-8-sig') as w4:
            for word in self.prefer_three_aop:
                w4.write(word + '\n')
        with open(three_aop_list_save_pat, 'w', encoding='utf-8-sig') as w5:
            for word in self.three_aop_list:
                w5.write(word + '\n')
        with open(prefer_four_aop_save_pat, 'w', encoding='utf-8-sig') as w6:
            for word in self.prefer_four_aop:
                w6.write(word + '\n')
        with open(four_aop_list_save_pat, 'w', encoding='utf-8-sig') as w7:
            for word in self.four_aop_list:
                w7.write(word + '\n')
        with open(two_repeat_one_save_pat, 'w', encoding='utf-8-sig') as w8:
            for word in self.two_repeat_one:
                w8.write(word + '\n')
        with open(three_repeat_one_save_pat, 'w', encoding='utf-8-sig') as w9:
            for word in self.three_repeat_one:
                w9.write(word + '\n')
        with open(four_repeat_one_save_pat, 'w', encoding='utf-8-sig') as w10:
            for word in self.four_repeat_one:
                w10.write(word + '\n')


class AOPCrawler(object):
    def __init__(self, get_dict_name='initial'):
        if get_dict_name == '':
            self.get_dict_name = 'initial'
        else:
            self.get_dict_name = get_dict_name
        self.current_path = os.getcwd()

    def aop_crawler(self):
        folder_name = self.get_dict_name
        dict_filepath = self.current_path + '\\' + folder_name
        aop_org_filepath = dict_filepath + '\\' + 'aop_org.csv'
        aop_org_df = pd.read_csv(aop_org_filepath)
        done_id_list = list(aop_org_df['AOP_id'])
        user_agent = UserAgent()
        header = {'user-agent': user_agent.random}
        url = 'https://aopwiki.org/aops.json'
        req = requests.get(url, headers=header)
        proper_json = json.loads(req.text)
        id_list = []
        with open(aop_org_filepath, 'a', encoding='utf-8-sig', newline='') as f:
            writer = csv.writer(f)
            for i, element in enumerate(proper_json):
                if element['id'] not in done_id_list:
                    id_list.append((i, element['id']))
            for get_id in id_list:
                url = f'https://aopwiki.org/aops/{get_id[1]}.json'
                scode = Spiders(url).get_content_from()
                datas = json.loads(scode)
                aop_aos = datas.get('aop_aos')
                aop_kes = datas.get('aop_kes')
                aop_mies = datas.get('aop_mies')
                aop_stressors = datas.get('aop_stressors')
                relationships = datas.get('relationships')
                tmp = [get_id[1]]
                try:
                    tmp.append(datas.get('title'))
                except:
                    tmp.append('')
                try:
                    tmp.append(datas.get('short_name'))
                except:
                    tmp.append('')
                for i in range(10):
                    if i < len(aop_aos):
                        tmp.append(aop_aos[i].get('event'))
                        tmp.append(aop_aos[i].get('event_id'))
                    else:
                        tmp.append('')
                        tmp.append('')
                for i in range(10):
                    if i < len(aop_kes):
                        tmp.append(aop_kes[i].get('event'))
                        tmp.append(aop_kes[i].get('event_id'))
                    else:
                        tmp.append('')
                        tmp.append('')
                for i in range(10):
                    if i < len(aop_mies):
                        tmp.append(aop_mies[i].get('event'))
                        tmp.append(aop_mies[i].get('event_id'))
                    else:
                        tmp.append('')
                        tmp.append('')
                for i in range(10):
                    if i < len(aop_stressors):
                        tmp.append(aop_stressors[i].get('stressor_id'))
                        tmp.append(aop_stressors[i].get('stressor_name'))
                    else:
                        tmp.append('')
                        tmp.append('')
                for i in range(10):
                    if i < len(relationships):
                        tmp.append(relationships[i].get('relation'))
                        tmp.append(relationships[i].get('upstream_event_id'))
                        tmp.append(relationships[i].get('upstream_event'))
                        tmp.append(relationships[i].get('downstream_event_id'))
                        tmp.append(relationships[i].get('downstream_event'))
                    else:
                        tmp.append('')
                        tmp.append('')
                        tmp.append('')
                        tmp.append('')
                        tmp.append('')
                writer.writerow(tmp)

    def append_aop_element(self):
        folder_name = self.get_dict_name
        dict_filepath = self.current_path + '\\' + folder_name
        element_id_aop = {}
        aop_element_filepath = dict_filepath + '\\' + 'aop_element.csv'
        aop_element_df = pd.read_csv(aop_element_filepath)
        aop_element_id = list(aop_element_df['aop_elements_id'])
        tmp_count = 0
        aop_org_filepath = dict_filepath + '\\' + 'aop_org.csv'
        aop_org_df = pd.read_csv(aop_org_filepath)
        for i in range(1, 11):
            element_id = list(aop_org_df[f'AOP_AO_id_{str(i)}'])
            element_aop = list(aop_org_df[f'AOP_AO_{str(i)}'])
            for index, get_id in enumerate(element_id):
                get_id = str(get_id)[:-2]
                if get_id not in element_id_aop and get_id != 'nan':
                    element_id_aop[get_id] = {'aop': element_aop[index], 'sort': 'AO'}
        for i in range(1, 11):
            element_id = list(aop_org_df[f'AOP_KE_id_{str(i)}'])
            element_aop = list(aop_org_df[f'AOP_KE_{str(i)}'])
            for index, get_id in enumerate(element_id):
                get_id = str(get_id)[:-2]
                if get_id not in element_id_aop and get_id != 'nan':
                    element_id_aop[get_id] = {'aop': element_aop[index], 'sort': 'KE'}
        for i in range(1, 11):
            element_id = list(aop_org_df[f'AOP_MIE_id_{str(i)}'])
            element_aop = list(aop_org_df[f'AOP_MIE_{str(i)}'])
            for index, get_id in enumerate(element_id):
                get_id = str(get_id)[:-2]
                if get_id not in element_id_aop and get_id != 'nan':
                    element_id_aop[get_id] = {'aop': element_aop[index], 'sort': 'MIE'}
        with open(aop_element_filepath, 'a', encoding='utf-8-sig', newline='') as w:
            csv_writ = csv.writer(w)
            for element_id in element_id_aop:
                if element_id not in aop_element_id and element_id and element_id != 'nan':
                    data = [element_id_aop[element_id]['aop'], element_id, element_id_aop[element_id]['sort'],
                            '', '', '', '', '', '', '', 'N']
                    csv_writ.writerow(data)
                    tmp_count += 1
        return tmp_count



class AOPMining(object):
    def __init__(self, get_dict_name='initial'):
        self.get_dict_name = get_dict_name
        one_aop_list = {}
        prefer_two_aop = {}
        two_aop_list = {}
        prefer_three_aop = {}
        three_aop_list = {}
        prefer_four_aop = {}
        four_aop_list = {}
        two_repeat_one = {}
        three_repeat_one = {}
        four_repeat_one = {}
        positive_trend = {}
        negative_trend = {}
        other_trend = {}
        all_trend = {}
        self.one_aop_list = one_aop_list
        self.prefer_two_aop = prefer_two_aop
        self.two_aop_list = two_aop_list
        self.prefer_three_aop = prefer_three_aop
        self.three_aop_list = three_aop_list
        self. prefer_four_aop = prefer_four_aop
        self.four_aop_list = four_aop_list
        self.two_repeat_one = two_repeat_one
        self.three_repeat_one = three_repeat_one
        self.four_repeat_one = four_repeat_one
        self.positive_trend = positive_trend
        self.negative_trend = negative_trend
        self.other_trend = other_trend
        self.all_trend = all_trend
        self.aop_dict = {}
        self.aop_id_element = {}
        self.load_dict()

    def load_dict(self):
        folder_name = self.get_dict_name
        current_path = os.getcwd()
        dict_filepath = current_path + '\\' + folder_name
        one_aop_list_save_path = dict_filepath + '\\' + 'one_aop_list' + '.txt'
        prefer_two_aop_save_path = dict_filepath + '\\' + 'prefer_two_aop' + '.txt'
        two_aop_list_save_pat = dict_filepath + '\\' + 'two_aop_list' + '.txt'
        prefer_three_aop_save_pat = dict_filepath + '\\' + 'prefer_three_aop' + '.txt'
        three_aop_list_save_pat = dict_filepath + '\\' + 'three_aop_list' + '.txt'
        prefer_four_aop_save_pat = dict_filepath + '\\' + 'prefer_four_aop' + '.txt'
        four_aop_list_save_pat = dict_filepath + '\\' + 'four_aop_list' + '.txt'
        two_repeat_one_save_pat = dict_filepath + '\\' + 'two_repeat_one' + '.txt'
        three_repeat_one_save_pat = dict_filepath + '\\' + 'three_repeat_one' + '.txt'
        four_repeat_one_save_pat = dict_filepath + '\\' + 'four_repeat_one' + '.txt'
        positive_trend_save_pat = dict_filepath + '\\' + 'positive_trend' + '.txt'
        negative_trend_save_pat = dict_filepath + '\\' + 'negative_trend' + '.txt'
        other_trend_save_pat = dict_filepath + '\\' + 'other_trend' + '.txt'
        all_trend_save_pat = dict_filepath + '\\' + 'Tendency' + '.txt'
        aop_dict_save_pat = dict_filepath + '\\' + 'aop_dict' + '.pkl'
        aop_id_element_save_pat = dict_filepath + '\\' + 'aop_id_element' + '.pkl'
        with open(one_aop_list_save_path, 'r', encoding='utf-8-sig') as f1:
            for line in f1.readlines():
                line = line.strip()
                self.one_aop_list[line] = 1
        with open(prefer_two_aop_save_path, 'r', encoding='utf-8-sig') as f2:
            for line in f2.readlines():
                line = line.strip()
                self.prefer_two_aop[line] = 1
        with open(two_aop_list_save_pat, 'r', encoding='utf-8-sig') as f3:
            for line in f3.readlines():
                line = line.strip()
                self.two_aop_list[line] = 1
        with open(prefer_three_aop_save_pat, 'r', encoding='utf-8-sig') as f4:
            for line in f4.readlines():
                line = line.strip()
                self.prefer_three_aop[line] = 1
        with open(three_aop_list_save_pat, 'r', encoding='utf-8-sig') as f5:
            for line in f5.readlines():
                line = line.strip()
                self.three_aop_list[line] = 1
        with open(prefer_four_aop_save_pat, 'r', encoding='utf-8-sig') as f6:
            for line in f6.readlines():
                line = line.strip()
                self.prefer_four_aop[line] = 1
        with open(four_aop_list_save_pat, 'r', encoding='utf-8-sig') as f7:
            for line in f7.readlines():
                line = line.strip()
                self.four_aop_list[line] = 1
        with open(four_repeat_one_save_pat, 'r', encoding='utf-8-sig') as f8:
            for line in f8.readlines():
                line = line.strip()
                self.four_repeat_one[line] = 1
        with open(two_repeat_one_save_pat, 'r', encoding='utf-8-sig') as f9:
            for line in f9.readlines():
                line = line.strip()
                self.two_repeat_one[line] = 1
        with open(three_repeat_one_save_pat, 'r', encoding='utf-8-sig') as f10:
            for line in f10.readlines():
                line = line.strip()
                self.three_repeat_one[line] = 1
        with open(positive_trend_save_pat, 'r', encoding='utf-8-sig') as f11:
            for line in f11.readlines():
                line = line.strip()
                self.positive_trend[line] = 1
        with open(negative_trend_save_pat, 'r', encoding='utf-8-sig') as f12:
            for line in f12.readlines():
                line = line.strip()
                self.negative_trend[line] = 1
        with open(other_trend_save_pat, 'r', encoding='utf-8-sig') as f13:
            for line in f13.readlines():
                line = line.strip()
                self.other_trend[line] = 1
        with open(all_trend_save_pat, 'r', encoding='utf-8-sig') as f14:
            for line in f14.readlines():
                line = line.strip()
                self.all_trend[line] = 1
        with open(aop_dict_save_pat, 'rb') as f:
            self.aop_dict = pickle.load(f)
        with open(aop_id_element_save_pat, 'rb') as f:
            self.aop_id_element = pickle.load(f)

    def double_lookup(self, word, token_word):
        word_index = [i for i, x in enumerate(token_word) if x == word]
        word_list = []
        for index in word_index:
            if index != len(token_word) - 1:
                double_word = word + ' ' + token_word[index + 1]
                if double_word in self.two_aop_list:
                    if double_word not in word_list:
                        word_list.append(double_word)
        return word_list

    def three_lookup(self, word, token_word):
        word_index = [i for i, x in enumerate(token_word) if x == word]
        word_list = []
        for index in word_index:
            if index != len(token_word) - 2 and index != len(token_word) - 1:
                three_word = word + ' ' + token_word[index + 1] + ' ' + token_word[index + 2]
                if three_word in self.three_aop_list:
                    if three_word not in word_list:
                        word_list.append(three_word)
        return word_list

    def four_lookup(self, word, token_word):
        word_index = [i for i, x in enumerate(token_word) if x == word]
        word_list = []
        for index in word_index:
            if index != len(token_word) - 2 and index != len(token_word) - 1 and index != len(token_word) - 3:
                four_word = word + ' ' + token_word[index + 1] + ' ' + token_word[index + 2] + ' ' + token_word[
                    index + 3]
                if four_word in self.four_aop_list:
                    if four_word not in word_list:
                        word_list.append(four_word)
        return word_list

    def word_lookup(self, read_content):
        once_aop = []
        once_trend = []
        sent_split = read_content.split()
        token_word = delete_characters(sent_split)
        for word in set(token_word):
            if word in self.prefer_two_aop:
                double_words = self.double_lookup(word, token_word)
                if len(double_words) != 0:
                    for double_word in double_words:
                        once_aop.append(double_word)
                        if double_word in self.all_trend and double_word not in once_trend:
                            once_trend.append(double_word)
                else:
                    if word in self.two_repeat_one:
                        once_aop.append(word)
            if word in self.prefer_three_aop:
                three_words = self.three_lookup(word, token_word)
                if len(three_words) != 0:
                    for three_word in three_words:
                        once_aop.append(three_word)
                        if three_word in self.all_trend and three_word not in once_trend:
                            once_trend.append(three_word)
                else:
                    if word in self.three_repeat_one:
                        once_aop.append(word)
            if word in self.prefer_four_aop:
                four_words = self.four_lookup(word, token_word)
                if len(four_words) != 0:
                    for four_word in four_words:
                        once_aop.append(four_word)
                        if four_word in self.all_trend and four_word not in once_trend:
                            once_trend.append(four_word)
                else:
                    if word in self.four_repeat_one:
                        once_aop.append(word)
            if word in self.one_aop_list:
                if word not in once_aop:
                    once_aop.append(word)
            if word in self.all_trend and word not in once_trend:
                once_trend.append(word)
        return once_aop, once_trend

    def aop_match(self, input_text):
        ner_aop_list = []
        get_aop_mark, get_aop_trend = self.word_lookup(input_text)
        if get_aop_mark:
            trend_list = []
            for trend in get_aop_trend:
                if trend in self.positive_trend:
                    if 'p' not in trend_list:
                        trend_list.append('p')
                elif trend in self.negative_trend:
                    if 'n' not in trend_list:
                        trend_list.append('n')
                elif trend in self.other_trend:
                    if trend not in trend_list:
                        trend_list.append(trend)
            for key in self.aop_dict:
                for mark_list in self.aop_dict[key]['mark']:
                    count = 0
                    for mark in mark_list:
                        if mark in get_aop_mark:
                            count += 1
                    if count == len(mark_list):
                        if self.aop_dict[key]['trend'] in trend_list:
                            if key not in ner_aop_list:
                                ner_aop_list.append(key)
                        else:
                            if self.aop_dict[key]['trend'] == 's':
                                if key not in ner_aop_list:
                                    ner_aop_list.append(key)
        return ner_aop_list

    def aop_ner(self, get_filepath, input_type='file'):
        if input_type == 'file':
            if fnmatch.fnmatch(get_filepath, '*.txt'):
                get_aop_list = []
                with open(get_filepath, 'r', encoding='utf-8-sig') as f:
                    for line in f.readlines():
                        line = line.strip()
                        sentences = sent_tokenize(line)
                        for sentence in sentences:
                            get_aop = self.aop_match(sentence)
                            if get_aop:
                                for aop in get_aop:
                                    if aop not in get_aop_list:
                                        get_aop_list.append(aop)
                print('---命名实体识别完成，识别结果如下：---')
                print(get_aop_list)
                return get_aop_list
            elif fnmatch.fnmatch(get_filepath, '*.pdf') or fnmatch.fnmatch(get_filepath, '*.PDF'):
                get_aop_list = []
                get_content = get_pdf_text(get_filepath)
                get_content = clean_text(get_content)
                sentences = sent_tokenize(get_content)
                for sentence in sentences:
                    get_aop = self.aop_match(sentence)
                    if get_aop:
                        for aop in get_aop:
                            if aop not in get_aop_list:
                                get_aop_list.append(aop)
                print('---命名实体识别完成，识别结果如下：---')
                print(get_aop_list)
                return get_aop_list
            else:
                print('---当前仅支持pdf, txt文件输入---')
        elif input_type == 'text':
            get_aop_list = self.aop_match(get_filepath)
            print('---命名实体识别完成，识别结果如下：---')
            print(get_aop_list)
            return get_aop_list
        elif input_type == 'folder':
            aop_filename = {}
            filename_aop = {}
            tmp_count = 1
            for filename in os.listdir(get_filepath):
                print('---当前处理第 %d 篇， 文件名为%s ---' % (tmp_count, filename))
                start = time()
                get_file_path = get_filepath + '\\' + filename
                with open(get_file_path, 'r', encoding='utf-8-sig') as f:
                    for line in f.readlines():
                        line = line.strip()
                        sentences = sent_tokenize(line)
                        for sentence in sentences:
                            get_aop = self.aop_match(sentence)
                            if get_aop:
                                for aop_id in get_aop:
                                    if aop_id not in aop_filename:
                                        aop_filename[aop_id] = []
                                    if filename not in aop_filename[aop_id]:
                                        aop_filename[aop_id].append(filename)
                                    if filename not in filename_aop:
                                        filename_aop[filename] = []
                                    if aop_id not in filename_aop[filename]:
                                        filename_aop[filename].append(aop_id)
                end = time()
                print('%s识别完毕，用时%.2f' % (filename, (end - start)))
                tmp_count += 1
            return aop_filename, filename_aop

    def output_file(self, get_filepath, input_type='file'):
        current_path = os.getcwd()
        save_filepath = current_path + '\\' + 'output'
        if not os.path.exists(save_filepath):
            os.makedirs(save_filepath)
        if input_type == 'file':
            get_aop_list = self.aop_ner(get_filepath, input_type='file')
            target_filepath = save_filepath + '\\' + 'aop_list.txt'
            with open(target_filepath, 'a', encoding='utf-8-sig') as w:
                for aop in get_aop_list:
                    w.write(aop + '\t' + self.aop_id_element[aop] + '\n')
            print('---文件保存完成，保存路径为%s---' % save_filepath)
        elif input_type == 'text':
            get_aop_list = self.aop_ner(get_filepath, input_type='text')
            target_filepath = save_filepath + '\\' + 'aop_list.txt'
            with open(target_filepath, 'a', encoding='utf-8-sig') as w:
                for aop in get_aop_list:
                    w.write(aop + '\t' + self.aop_id_element[aop] + '\n')
        elif input_type == 'folder':
            aop_filename, filename_aop = self.aop_ner(get_filepath, input_type='folder')
            aop_filename_save_path = save_filepath + '\\' + 'aop_filename.csv'
            aop_filename_save_path_pkl = save_filepath + '\\' + 'aop_filename.pkl'
            with open(aop_filename_save_path, 'a', encoding='utf-8-sig', newline='') as w1:
                csv_writer = csv.writer(w1)
                data = ['AOP_id', 'AOP', 'Frequency', 'List']
                csv_writer.writerow(data)
                for key in aop_filename:
                    data = [key, self.aop_id_element[key], len(aop_filename[key]), ' | '.join(aop_filename[key])]
                    csv_writer.writerow(data)
            with open(aop_filename_save_path_pkl, 'wb') as w1_pkl:
                pickle.dump(aop_filename, w1_pkl)
            filename_aop_save_path = save_filepath + '\\' + 'filename_aop.csv'
            filename_aop_save_path_pkl = save_filepath + '\\' + 'filename_aop.pkl'
            with open(filename_aop_save_path, 'a', encoding='utf-8-sig', newline='') as w3:
                csv_writer = csv.writer(w3)
                data = ['Filename', 'Reported AOPs', 'List']
                csv_writer.writerow(data)
                for key in filename_aop:
                    data = [key, len(filename_aop[key]), ' | '.join(filename_aop[key])]
                    csv_writer.writerow(data)
            with open(filename_aop_save_path_pkl, 'wb') as w3_pkl:
                pickle.dump(filename_aop, w3_pkl)
            print('---文件保存完成，保存路径为%s---' % save_filepath)
        else:
            print('---未识别到该输入类型，请重新输入。输入类型包括：文本：text，文件：file，文件夹：folder---')


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.band()
        self.initial_dict = AOPMining()

    def band(self):
        self.ui.new_dict.clicked.connect(self.new_dict)
        self.ui.clean_button_input.clicked.connect(self.clean_text)
        self.ui.clean_output_process.clicked.connect(self.clean_output)
        self.ui.clean_dict_name.clicked.connect(self.clean_dict)
        self.ui.load_dict.clicked.connect(self.load_dict)
        self.ui.start_ner.clicked.connect(self.start_ner)
        self.ui.ner_output.clicked.connect(self.ner_output)
        self.ui.aop_crawler.clicked.connect(self.renew_aop)

    def new_dict(self):
        input_text = self.ui.input_text.text()
        input_type = self.ui.input_type.currentText()
        dict_name = self.ui.input_dict_name.text()
        if input_type == '词典':
            generate_dict = GenerateDict(input_text, dict_name)
            generate_dict.new_dict()
            tmp_text = '---新建词典成功---'
            self.ui.output_text.setText('')
            self.ui.output_text.setText(tmp_text)
        else:
            self.ui.output_text.setText('')
            self.ui.output_text.setText('当前输入类型非词典类型，无法新建词典')

    def clean_text(self):
        self.ui.input_text.setText('')

    def clean_dict(self):
        self.ui.input_dict_name.setText('')

    def clean_output(self):
        self.ui.output_text.setText('')

    def load_dict(self):
        dict_name = self.ui.input_dict_name.text()
        if dict_name:
            current_path = os.getcwd()
            if dict_name in os.listdir(current_path):
                self.ui.output_text.setText('')
                self.initial_dict = AOPMining(dict_name)
                self.ui.output_text.setText('---词典加载完成，可进行下一步命名实体识别---')
            else:
                self.ui.output_text.setText('')
                self.ui.output_text.setText('---无对应词典，请检查输入词典名称---')
        else:
            self.ui.output_text.setText('')
            self.initial_dict = AOPMining()
            self.ui.output_text.setText('---词典加载完成，可进行下一步命名实体识别---')

    def start_ner(self):
        input_text = self.ui.input_text.text()
        input_type = self.ui.input_type.currentText()
        if input_type == '文件':
            self.ui.output_text.setText('')
            get_text = self.initial_dict.aop_ner(input_text, input_type='file')
            get_text = ' | '.join(get_text)
            self.ui.output_text.setText(get_text)
        elif input_type == '文本':
            self.ui.output_text.setText('')
            get_text = self.initial_dict.aop_ner(input_text, input_type='text')
            get_text = ' | '.join(get_text)
            self.ui.output_text.setText(get_text)
        elif input_type == '文件夹':
            self.ui.output_text.setText('')
            get_text = self.initial_dict.aop_ner(input_text, input_type='folder')
            for i in get_text:
                tmp_output = str(i)
                self.ui.output_text.setText(tmp_output)
        else:
            self.ui.output_text.setText('')
            self.ui.output_text.setText('---当前输入类型不支持进行命名实体识别，请重新设置')

    def ner_output(self):
        current_path = os.getcwd()
        save_filepath = current_path + '\\' + 'output'
        input_text = self.ui.input_text.text()
        input_type = self.ui.input_type.currentText()
        if input_type == '文件':
            self.initial_dict.output_file(input_text, input_type='file')
            self.ui.output_text.setText('')
            self.ui.output_text.setText('识别完成，文件保存位置为：%s' % save_filepath)
        elif input_type == '文本':
            self.initial_dict.output_file(input_text, input_type='text')
            self.ui.output_text.setText('')
            self.ui.output_text.setText('识别完成，文件保存位置为：%s' % save_filepath)
        elif input_type == '文件夹':
            self.initial_dict.output_file(input_text, input_type='folder')
            self.ui.output_text.setText('')
            self.ui.output_text.setText('识别完成，文件保存位置为：%s' % save_filepath)
        else:
            self.ui.output_text.setText('')
            self.ui.output_text.setText('---当前输入类型不支持进行命名实体识别，请重新设置---')

    def renew_aop(self):
        dict_name = self.ui.input_dict_name.text()
        renew_aop_crawler = AOPCrawler(dict_name)
        renew_aop_crawler.aop_crawler()
        get_count = renew_aop_crawler.append_aop_element()
        self.ui.output_text.setText('更新AOP完成，需要标注的AOP术语有%s条' % str(get_count))


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
