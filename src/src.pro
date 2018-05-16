TARGET = nemopolicy
PLUGIN_IMPORT_PATH = Nemo/Policy

TEMPLATE = lib
CONFIG += qt plugin hide_symbols link_pkgconfig
QT -= gui
QT += qml

target.path = $$[QT_INSTALL_QML]/$$PLUGIN_IMPORT_PATH
INSTALLS += target

qmldir.files += qmldir plugins.qmltypes
qmldir.path +=  $$target.path
INSTALLS += qmldir

qmltypes.commands = qmlplugindump -nonrelocatable Nemo.Policy 1.0 > $$PWD/plugins.qmltypes
QMAKE_EXTRA_TARGETS += qmltypes

PKGCONFIG += libresourceqt5

SOURCES += \
        plugin.cpp \
        permissions.cpp \
        resource.cpp

HEADERS += \
        permissions.h \
        resource.h

