project(plugins)

set(CMAKE_INCLUDE_CURRENT_DIR ON)

set(CMAKE_AUTOMOC ON)

find_package(Qt6 COMPONENTS Core Gui Widgets UiPlugin)

set(ui_plugin_src
    customwidgets.cpp
    customwidget.cpp
)

add_library(uiplugin STATIC ${ui_plugin_src})
if(CMAKE_HOST_UNIX AND NOT CYGWIN)
    add_definitions(-fPIC)
endif()
add_definitions(-DQT_STATICPLUGIN)

set_property(TARGET pyside6 PROPERTY CXX_STANDARD 17)

target_link_libraries(uiplugin
                      Qt::Core
                      Qt::Gui
                      Qt::UiPlugin
                      Qt::Widgets
                      Shiboken6::libshiboken)
if (CMAKE_BUILD_TYPE STREQUAL "Debug")
    set(LIBRARY_OUTPUT_SUFFIX ${CMAKE_DEBUG_POSTFIX})
else()
    set(LIBRARY_OUTPUT_SUFFIX ${CMAKE_RELEASE_POSTFIX})
endif()
