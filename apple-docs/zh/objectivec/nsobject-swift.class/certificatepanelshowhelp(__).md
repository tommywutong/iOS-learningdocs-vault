---
title: 'certificatePanelShowHelp(_:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/certificatepanelshowhelp(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/certificatepanelshowhelp(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/certificatepanelshowhelp%28_%3A%29.json'
content_hash: 'sha256:914d7c20d95da044'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# certificatePanelShowHelp(_:)

<sub>实例方法</sub>

为实现该模态面板实现自定义帮助行为。

<sub>macOS</sub>

```swift
func certificatePanelShowHelp(_ sender: SFCertificatePanel!) -> Bool
```

## 参数

- `sender` — 要实现自定义帮助的证书面板。

## 讨论

若你调用 [setShowsHelp(_:)](<../../securityinterface/sfcertificatepanel/setshowshelp(__).md>) 方法以在表单或面板中显示帮助按钮，则可以使用此委托方法实现自定义帮助。若不实现自定义帮助，请勿实现此方法。

## 另请参阅

### 相关文档

- [delegate](../../appkit/nswindow/delegate.md) — 窗口的委托。
- [setShowsHelp(_:)](<../../securityinterface/sfcertificatepanel/setshowshelp(__).md>) — 在表单或面板中显示帮助按钮。
