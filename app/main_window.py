from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QLineEdit,
    QTextEdit,
    QFrame
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("DJoker AI")
        self.resize(1400, 850)

        self.setStyleSheet("""
            QMainWindow{
                background:#0b0f19;
            }

            QWidget{
                background:#0b0f19;
                color:white;
                font-size:14px;
            }

            QPushButton{
                background:#171d2d;
                border:none;
                border-radius:10px;
                padding:12px;
                color:white;
            }

            QPushButton:hover{
                background:#242d45;
            }

            QLineEdit{
                background:#171d2d;
                border:1px solid #303b58;
                border-radius:12px;
                padding:12px;
                color:white;
            }

            QTextEdit{
                background:#111726;
                border:none;
                border-radius:12px;
                color:white;
                padding:10px;
            }

            QFrame{
                background:#131a29;
                border-radius:15px;
            }
        """)

        root = QWidget()
        self.setCentralWidget(root)

        layout = QHBoxLayout(root)

        # ---------- LEFT MENU ----------

        left = QFrame()
        left.setFixedWidth(220)

        left_layout = QVBoxLayout(left)

        title = QLabel("DJoker AI")
        title.setFont(QFont("Segoe UI",18,QFont.Bold))
        title.setAlignment(Qt.AlignCenter)

        left_layout.addWidget(title)

        buttons = [
            "💬 Chats",
            "🌐 Internet",
            "🎵 Music AI",
            "🎬 Video AI",
            "🖼 Image AI",
            "💻 PC Control",
            "⚙ Settings"
        ]

        for text in buttons:
            left_layout.addWidget(QPushButton(text))

        left_layout.addStretch()

        # ---------- CENTER ----------

        center = QWidget()
        center_layout = QVBoxLayout(center)

        logo = QLabel("◉")
        logo.setAlignment(Qt.AlignCenter)
        logo.setStyleSheet("""
            font-size:120px;
            color:#7b5cff;
        """)

        state = QLabel("DJoker AI Ready")
        state.setAlignment(Qt.AlignCenter)
        state.setFont(QFont("Segoe UI",18))

        self.chat = QTextEdit()
        self.chat.setReadOnly(True)

        self.chat.append("Welcome to DJoker AI.")

        self.input = QLineEdit()
        self.input.setPlaceholderText("Write your message...")

        send = QPushButton("Send")

        center_layout.addStretch()
        center_layout.addWidget(logo)
        center_layout.addWidget(state)
        center_layout.addStretch()
        center_layout.addWidget(self.chat)
        center_layout.addWidget(self.input)
        center_layout.addWidget(send)

        # ---------- RIGHT ----------

        right = QFrame()
        right.setFixedWidth(240)

        right_layout = QVBoxLayout(right)

        status = QLabel("System")
        status.setFont(QFont("Segoe UI",16,QFont.Bold))

        right_layout.addWidget(status)
        right_layout.addSpacing(20)

        right_layout.addWidget(QLabel("🟢 AI Ready"))
        right_layout.addWidget(QLabel("🌐 Internet"))
        right_layout.addWidget(QLabel("💾 Memory"))
        right_layout.addWidget(QLabel("🧠 Brain"))
        right_layout.addStretch()

        layout.addWidget(left)
        layout.addWidget(center)
        layout.addWidget(right)