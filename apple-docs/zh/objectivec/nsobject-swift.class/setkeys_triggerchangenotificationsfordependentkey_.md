---
title: 'setKeys:triggerChangeNotificationsForDependentKey:'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [macOS 10.0+（10.5 起废弃）]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/objectivec/nsobject-swift.class/setkeys:triggerchangenotificationsfordependentkey:'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/setkeys:triggerchangenotificationsfordependentkey:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/setkeys%3Atriggerchangenotificationsfordependentkey%3A.json'
content_hash: 'sha256:fa2cc0f023e0e1a7'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# setKeys:triggerChangeNotificationsForDependentKey:

<sub>类型方法</sub>

配置被观察对象，以便在给定数组中指定的任何属性更改时，为给定属性发送更改通知。

> [!warning] 已废弃
> Use the method [+ keyPathsForValuesAffectingValueForKey:](<keypathsforvaluesaffectingvalue(forkey_).md>) instead.

<sub>macOS</sub>

```objc
+ (void) setKeys:(NSArray *) keys triggerChangeNotificationsForDependentKey:(NSString *) dependentKey;
```

## 参数

- `keys` — 由 `dependentKey` 标识的属性的值所依赖的属性的名称。

- `dependentKey` — 其值依赖于 `keys` 指定的属性的属性的名称。

## 讨论

对 `keys` 中任何键的 will- 和 did-change KVO 通知方法的调用会自动调用 `dependentKey` 的相应更改通知方法。被观察对象不会收到用于生成通知的 `willChange` 或 `didChange` 消息。

应在创建接收类的任何实例之前注册依赖关系，因此你通常在类的 [+ initialize](<initialize().md>) 方法中调用此方法，如下例所示。

```objc
+ (void)initialize {
    [self setKeys:@[@"firstName", @"lastName"] triggerChangeNotificationsForDependentKey:@"fullName"];
}
```

## 另请参阅

### 已废弃的类方法

- [+ defaultPlaceholderForMarker:withBinding:](<defaultplaceholder(for_with_).md>) — 当接收类实例的符合键值编码的属性返回 `marker` 指定的值，且尚未指定其他占位符时，返回将用作 `binding` 占位符的对象。 _(已废弃)_
- [+ setDefaultPlaceholder:forMarker:withBinding:](<setdefaultplaceholder(__for_with_).md>) — 当接收类实例的符合键值编码的属性返回由 `marker` 指定的值，且尚未指定其他占位符时，将 `placeholder` 设为 `binding` 的默认占位符。 _(已废弃)_
- [+ useStoredAccessor](<usestoredaccessor().md>) — 若存储值方法 [- storedValueForKey:](<storedvalue(forkey_).md>) 和 [- takeStoredValue:forKey:](<takestoredvalue(__forkey_).md>) 应优先使用私有访问器方法而非公共访问器，则返回 `true`。 _(已废弃)_
