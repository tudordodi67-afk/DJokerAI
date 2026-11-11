import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow {
    visible: true
    width: 1600
    height: 900
    title: "DJoker AI - Nexus Core"
    color: "#0c2196"

    Rectangle {
        anchors.fill: parent
        color: "#0e9725"

        RowLayout{
            anchors.fill: parent

            Rectangle{
                Layout.preferredWidth:250
                Layout.fillHeight:true
                color:"#db0a73"

                Column{
                    anchors.fill: parent
                    anchors.margins:20
                    spacing:15

                    Label{
                        text:"DJoker AI"
                        color:"white"
                        font.pixelSize:28
                        font.bold:true
                    }

                    Button{text:"💬 Chat"}
                    Button{text:"🌐 Internet"}
                    Button{text:"🎵 Music AI"}
                    Button{text:"🎥 Video AI"}
                    Button{text:"🖼 Image AI"}
                    Button{text:"⚙ Settings"}
                }
            }

            Rectangle{
                Layout.fillWidth:true
                Layout.fillHeight:true
                color:"#101010"

                Column{
                    anchors.fill: parent
                    anchors.margins:20
                    spacing:15

                    Label{
                        text:"NEXUS CORE"
                        color:"#9d4dff"
                        font.pixelSize:36
                        font.bold:true
                    }

                    TextArea{
                        id:chat
                        readOnly:true
                        text:"Добро пожаловать в DJoker AI\n\n"
                        color:"white"

                        background: Rectangle{
                            color:"#202020"
                            radius:10
                        }

                        Layout.fillWidth:true
                        Layout.fillHeight:true
                    }

                    Row{
                        spacing:10

                        TextField{
                            id:input
                            width:900
                            placeholderText:"Введите сообщение..."
                        }

                        Button{
                            text:"Отправить"

                            onClicked:{
                                chat.text += "Вы: " + input.text + "\n"
                                input.text=""
                            }
                        }
                    }
                }
            }
        }
    }
}