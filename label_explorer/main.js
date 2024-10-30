const { app, BrowserWindow, ipcMain, Menu } = require('electron')
const path = require('node:path')

const menuItems = [
    {
        label: "文件",
        submenu: [
            {
                label: "上传文件"
            },
            {
                label: "打开摄像头 ",
                click: async () => {
                    const { BrowserWindow } = require('electron')
                    const win2 = new BrowserWindow({
                        height: 300,
                        width: 400,
                        show: false,
                    });

                    // win2.webContents.openDevTools();
                    win2.loadFile("camera.html");
                    // win2.loadURL("https://github.com")
                    win2.once('ready-to-show', () => {
                        win2.show();
                    })

                }
            },
            {
                label: "新建窗口",
                click: async () => {
                    const { BrowserWindow } = require('electron')
                    const win2 = new BrowserWindow({
                        height: 300,
                        width: 400,
                        show: false,
                    });
                    win2.loadFile("index2.html");
                    // win2.loadURL("https://github.com")
                    win2.once('ready-to-show', () => {
                        win2.show();
                    })

                }
            }
        ]
    },
    {
        label: "我们",
        submenu: [
            {
                label: "项目地址",
                click: async () => {
                    const { shell } = require('electron')
                    await shell.openExternal('https://gitee.com/intelligence-vision/label-explorer')
                },
            },
            {
                type: "separator",
            },
            {
                label: "退出",
                click: () => app.quit(),
            },
        ]
    },
    {
        label: "Window",
        submenu: [
            {
                role: "minimize",
            },
            {
                role: "close",
            },
        ]
    }
]

const menu = Menu.buildFromTemplate(menuItems);
Menu.setApplicationMenu(menu);

const createWindow = () => {
    const win = new BrowserWindow({
        width: 800,
        height: 600,
        webPreferences: {
            preload: path.join(__dirname, 'preload.js')
        }
    })

    win.loadFile('index.html')
}

app.whenReady().then(() => {
    // ipcMain.handle('ping', () => 'pong')
    createWindow()

    app.on('activate', () => {
        if (BrowserWindow.getAllWindows().length === 0) {
            createWindow()
        }
    })
})

app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') {
        app.quit()
    }
})
