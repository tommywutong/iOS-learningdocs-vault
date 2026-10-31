---
title: 'commitEditingWithDelegate:didCommitSelector:contextInfo:'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.0+（11.0 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: '/documentation/objectivec/nsobject-swift.class/commiteditingwithdelegate:didcommitselector:contextinfo:'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/commiteditingwithdelegate:didcommitselector:contextinfo:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/commiteditingwithdelegate%3Adidcommitselector%3Acontextinfo%3A.json'
content_hash: 'sha256:cf0a5fc73d47e8e9'
translated: true
---
> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# commitEditingWithDelegate:didCommitSelector:contextInfo:

<sub>实例方法</sub>

尝试提交接收者当前正在编辑的任何结果。

<sub>Mac Catalyst, macOS</sub>

```objc
- (void) commitEditingWithDelegate:(id) delegate didCommitSelector:(SEL) didCommitSelector contextInfo:(void *) contextInfo;
```

## 讨论

接收者必须已通过 `objectDidBeginEditing:` 注册为对象的编辑器，且尚未被后续的 `objectDidEndEditing:` 调用取消注册。当提交成功或失败时，向指定对象发送以下消息。`didCommitSelector` 方法必须具有以下方法签名：

```objc
- (void)editor:(id)editor didCommit:(BOOL)didCommit contextInfo:(void *)contextInfo
```

如果在尝试提交时发生错误，例如键值编码验证失败，此方法的实现通常应向正在进行编辑的 NSView 发送 `presentError:modalForWindow:delegate:didRecoverSelector:contextInfo:` 消息，并指定该视图的包含窗口。
