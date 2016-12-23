TARGET = nemopolicy
PLUGIN_IMPORT_PATH = org/nemomobile/policy

TEMPLATE = lib
CONFIG += qt plugin hide_symbols link_pkgconfig
QT -= gui
QT += qml

target.path = $$[QT_INSTALL_QML]/$$PLUGIN_IMPORT_PATH
INSTALLS += target

qmldir.files += $$_PRO_FILE_PWD_/qmldir
qmldir.path +=  $$target.path
INSTALLS += qmldir

PKGCONFIG += libresourceqt5

SOURCES += \
        plugin.cpp \
        permissions.cpp \
        resource.cpp

HEADERS += \
        permissions.h \
        resource.h

