# Switch-Fightstick
參考自 [wwwwwwzx/Switch-Fightstick](https://github.com/wwwwwwzx/Switch-Fightstick)

## 必須物品
- Arduino UNO R3
- USB to TTL
- USB線
- 杜邦線 公-公 1條
- 杜邦線 公-母 5條

## 選配物品
- Usb to Type-C 轉接頭

## 注意事項
- 如果有 **Usb to Type-C 轉接頭** 的話就不需要 Switch Dock

## 使用方法
- 燒錄 **[Joystick.hex](https://github.com/k88097/Switch-Fightstick/blob/master/Joystick.hex)** 進入 Arduino
- USB to TTL 接法:  
		5V -> 5V  
		GND -> GND  
		RXD -> RX  
		TX -> TX  
		3.3V -> 3.3V
- 電腦 -> 連接器 -> Arduino (-> Switch Dock) -> Switch
- 使用 **example** 中的程式控制 **Switch**

## 程式功能說明 
**所有[範例程式](https://github.com/k88097/Switch-Fightstick/tree/master/example)僅限適用於遊戲為繁體中文版(CHT)與主機語言為中文。**
|程式檔名|功能說明|
|:---:|:---:|
|**Simple_example** | 連續按 10次 A鍵|
|**Fossil** | 自動復活化石|
|**Hatching_egg_on_5_road**|自動取蛋(僅限五號道路)|