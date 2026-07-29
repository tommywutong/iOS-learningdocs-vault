---
title: 定义启动环境和库约束
framework: Security
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/defining-launch-environment-and-library-constraints
source_url: 'https://developer.apple.com/documentation/security/defining-launch-environment-and-library-constraints'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/defining-launch-environment-and-library-constraints.json'
content_hash: 'sha256:55f384318d921926'
translated: true
---

> 导航：[技术](../technologies.md) · [安全](../security.md)

# 定义启动环境和库约束

<sub>文章</sub>

将 App 的组件限制在其预期的上下文中。

## 概述

你可以在约束字典中定义启动环境和库约束，这些字典要么保存在 `launchd` 属性列表文件中，要么保存在用于代码签名的独立属性列表文件中。你创建的约束字典包含_事实_和_操作_。事实是指定操作系统正在启动的可执行文件或你的进程加载的库的某些属性符合你指定条件的断言。操作允许对事实进行丰富组合。

约束字典的顶层隐式地包含一个 `$and` 操作，它包含字典中的所有事实和操作。当一个进程尝试启动另一个进程——通过调用 `execve(_:_:_:)` 或 `posix_spawn(_:_:_:_:_:_:)`——操作系统会检查可执行文件是否满足其自身的自身约束（self constraint）。它还会检查父进程的可执行文件是否满足可执行文件的父约束（parent constraint），以及负责进程的可执行文件是否满足可执行文件的负责进程约束（responsible process constraint）。如果这些启动约束中的任何一个不满足，操作系统就不会运行该程序。

如果库约束字典顶层所有的事实和操作对于包含该库的文件都为真，那么你的进程可以加载该动态库。如果库约束的任何部分不为真，你的进程就不会加载该库。

当 `launchd` 需要启动你的启动守护程序或代理时，它会测试你在 `launchd` 属性列表文件中指定的约束。如果 `launchd` 属性列表中指定的可执行文件不满足属性列表中的约束，那么 `launchd` 就不会启动该进程。

### 约束可执行文件的启动环境

通过添加表示约束事实的键和值，以及使用逻辑运算组合事实的操作符，来构造启动约束。在你的启动约束中使用以下列表中的事实。

- **`cdhash`** — 一个二进制数据序列，是可执行文件代码目录内容的哈希值；或者是一个 `$in` 操作符，其参数是一个数据序列列表。如果可执行文件的代码目录哈希值与约束中的值相同，则满足此约束。有关代码目录哈希值的更多信息，请参阅 [TN3126: 代码签名内部原理：哈希值](../technotes/tn3126-inside-code-signing-hashes.md)。

单个可执行文件可以包含多个代码目录哈希值，用于不同的 CPU 架构和哈希算法。使用有效哈希值的集合和 `$in` 操作来标识可执行文件的代码目录哈希值。

- **`entitlements`** — 一个 entitlements 查询，指定一个 entitlement 并给出其期望值。如果可执行文件的代码签名包含具有指定值的此 entitlement，则满足此约束。有关 entitlement 列表，请参阅 [Entitlements](../bundleresources/entitlements.md)。有关如何构造 entitlements 查询的信息，请参阅下面的 `$query` 操作符。
- **`is-init-proc`** — 一个布尔值，指示该可执行文件是否必须是操作系统的初始化进程（`launchd`）。
- **`is-sip-protected`** — 一个布尔值，指示该可执行文件是否必须是由系统完整性保护（SIP）保护的文件。
- **`launch-type`** — 一个整数值，描述操作系统启动可执行文件的上下文。启动类型 0 是默认值，表示操作系统未设置启动类型。从 macOS 14.0 开始，当启动可执行文件以启动 App 时，例如，当用户在程序坞中点击 App 图标时，Launch Services 会设置启动类型 3。启动类型 1 和 2 保留供操作系统使用。
- **`on-authorized-authapfs-volume`** — 一个布尔值，指示操作系统是否从已授权、经认证的 APFS 宗卷加载了该可执行文件。
- **`on-system-volume`** — 一个布尔值，指示操作系统是否从当前引导的系统宗卷加载了该可执行文件。
- **`signing-identifier`** — 一个字符串，是代码签名标识符；或者是一个 `$in` 操作符，其参数是一个字符串列表。如果可执行文件的签名标识符与约束中的值相同，则满足此约束。可执行文件的代码签名标识符通常是包含该可执行文件的 bundle 的信息属性列表中的 [CFBundleIdentifier](../bundleresources/information-property-list/cfbundleidentifier.md)。
- **`team-identifier`** — 一个标识注册开发者的字符串；或者是一个 `$in` 操作符，其参数是一个字符串列表。如果签署该可执行文件的团队与约束中的值匹配，则满足此约束。

团队标识符存在于由开发、TestFlight、App Store 或 Developer ID 的代码签名身份签署的可执行文件中。

- **`validation-category`** — 一个整数，是代码签名验证类别；或者是一个 `$in` 操作符，其参数是一个整数列表。如果可执行文件的签名与约束中的验证类别一致，则满足此约束。使用下表中验证类别的值。

将下表中的值与 `validation-category` 事实一起使用。

| 代码签名验证类别 | 描述 |
|---|---|
| `1` | 一个操作系统可执行文件。 |
| `2` | 一个通过 TestFlight 分发的可执行文件。 |
| `3` | 一个由开发代码签名身份签署的可执行文件。 |
| `4` | 一个通过 App Store 分发的可执行文件。 |
| `5` | 一个使用企业通用预置描述文件或 ad-hoc 分发方式分发的可执行文件。 |
| `6` | 一个使用 Developer ID 签署的可执行文件。 |
| `7`、`8` 或 `9` | 这些值不适用于约束中的 `validation-category` 事实，因为它们代表系统在某些受限情况下生成的二进制文件的类别。 |
| `10` | 一个使用不匹配任何其他类别的代码签名身份签署的可执行文件。 |

这个启动约束示例使用 `team-identifier` 事实，要求可执行文件使用团队 ID `8XCUU22SN2` 签署。

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>team-identifier</key>
  <string>8XCUU22SN2</string>
</dict>
</plist>
```

### 使用操作符构建复杂检查

约束字典可以包含以下任何操作符，以构建复杂的检查。操作符可以在事实中替代值的位置，在这种情况下，操作符表达式中的每个值都应用于包含该操作符的事实。操作符也可以替代事实键本身的位置，在这种情况下，操作符表达式的值本身就是命名事实的键值对。由于字典仅包含任何特定键的一个实例，因此使用操作符来组合使用同一事实的多个测试。

| 操作符 | 值类型 | 描述 |
|---|---|---|
| `$and` | 一个事实或操作符的字典。 | 如果每个子表达式都为真，则 `$and` 操作为真。 |
| `$and-array` | 一个子数组的数组。每个子数组包含一个逻辑操作符（`$and`、`$or` 或 `$optional`），后跟一个事实或操作的字典。 | 如果每个子表达式都为真，则 `$and-array` 操作为真。使用 `$and-array` 来简化需要使用 `$and` 进行多层嵌套的表达式。 |
| `$or` | 一个事实或操作符的字典。 | 如果任意子表达式为真，则 `$or` 操作为真。 |
| `$or-array` | 一个子数组的数组。每个子数组包含一个逻辑操作符（`$and`、`$or` 或 `$optional`），后跟一个事实或操作的字典。 | 如果任意子表达式为真，则 `$or-array` 操作为真。使用 `$or-array` 来简化需要使用 `$or` 进行多层嵌套的表达式。 |
| `$in` | 一个字符串、数据或整数的列表。 | 如果事实的值是该列表的成员，则使用 `$in` 操作符的事实成立。 |
| `$lt` | 一个整数。 | 如果事实的值小于指定的值，则使用 `$lt` 操作符的事实成立。 |
| `$lte` | 一个整数。 | 如果事实的值小于或等于指定的值，则使用 `$lte` 操作符的事实成立。 |
| `$gt` | 一个整数。 | 如果事实的值大于指定的值，则使用 `$gt` 操作符的事实成立。 |
| `$gte` | 一个整数。 | 如果事实的值大于或等于指定的值，则使用 `$gte` 操作符的事实成立。 |
| `$optional` | 一个包含单个事实或操作符的字典。 | `$optional` 操作符的结果取决于该操作符的上下文。在 `$or` 和 `$or-array` 操作符内部，仅当包含的事实或操作符为真时，`$optional` 才为真。在所有其他上下文中——包括在 `$and` 或 `$and-array` 操作符内部——当包含的事实或操作符的值为真，或该值不确定时，`$optional` 为真。 |
| `$query` | 一个包含子数组的数组，用于表示 entitlements 查询。 | 内核使用该查询来测试可执行文件的 entitlements。你只能将 `$query` 操作符用作 `entitlements` 事实的值。要了解在 entitlements 查询中可以使用的操作符和值，请参阅下面的构造 entitlements 查询。 |

下面示例中的启动约束使用 `$or` 操作符，要求可执行文件要么使用团队 ID `8XCUU22SN2` 签署，要么是操作系统可执行文件。

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>$or</key>
  <dict>
    <key>team-identifier</key>
    <string>8XCUU22SN2</string>
    <key>validation-category</key>
    <integer>1</integer>
  </dict>
</dict>
</plist>
```

### 构造 entitlements 查询

一个 entitlements 查询是一个查询操作构成的数组。每个操作是一个包含两个条目的数组：一个整数操作码和一个参数，该参数可以是整数、字符串或布尔值。这些操作要么选择有关 entitlements 的特定信息，要么将当前选中的信息与参数中指定的值进行匹配。

内核在一个虚拟机（VM）中执行你的查询，该虚拟机具有包含 entitlements 状态和有效性标志的上下文。状态的初始值是可执行文件的 entitlements 字典，并且查询执行是有效的。VM 依次处理查询中的每个操作。选择操作通过从当前状态中获取特定信息来更新状态，如果找不到请求的信息，则将执行标记为无效。如果当前状态的值与操作的参数匹配，则匹配操作将执行标记为有效，否则标记为无效。如果执行保持有效，直到 VM 执行完查询中的所有操作，则可执行文件满足该查询。

在 entitlements 查询中使用以下操作码：

| 操作码 | 操作 | 值类型 | 描述 |
|---|---|---|---|
| `1` | 选择键 | 一个命名字典键的字符串 | 如果当前状态是包含此键的字典，则该操作将状态更新为该键在字典中的值。如果当前状态不是字典或不包含此键，则该操作将查询执行标记为无效。 |
| `2` | 选择索引 | 一个表示数组索引的整数 | 如果当前状态是一个包含足够元素的数组，则该操作将状态更新为数组中给定索引处的值。如果索引不在数组中或当前状态不是数组，则该操作将查询执行标记为无效。 |
| `3` | 匹配字符串 | 一个字符串 | 如果当前状态是一个等于参数的字符串，则将执行标记为有效；否则，标记为无效。 |
| `4` | 匹配字符串前缀 | 一个字符串 | 如果当前状态是一个以参数开头的字符串，则将执行标记为有效；否则，标记为无效。 |
| `5` | 匹配布尔值 | 一个布尔值 | 如果当前状态是一个等于参数的布尔值，则将执行标记为有效；否则，标记为无效。 |
| `6` | 允许的字符串值 | 一个字符串 | 如果当前状态是字符串，则此操作等同于匹配字符串（上面的操作码 `3`）。如果当前状态是一个字符串列表，并且列表中的任何元素等于参数，则将执行标记为有效。 |
| `7` | 匹配整数 | 一个整数 | 如果当前状态是一个等于参数的整数，则将执行标记为有效；否则，标记为无效。 |
| `8` | 允许的字符串前缀值 | 一个字符串 | 如果当前状态是字符串，则此操作等同于匹配字符串前缀（上面的操作码 `4`）。如果当前状态是一个字符串列表，并且列表中的任何元素等于参数，则将执行标记为有效。 |
| `9` | 使用前缀选择键 | 一个命名字典键的字符串 | 如果当前状态是一个包含任何以参数开头的键的字典，则该操作将状态更新为字典中匹配最长键的值。如果当前状态不是字典或不包含具有此前缀的键，则该操作将查询执行标记为无效。 |
| `10` | 允许的整数值 | 一个整数 | 如果当前状态是整数，则此操作等同于匹配整数（上面的操作码 `7`）。如果当前状态是一个整数列表，并且列表中的任何元素等于参数，则将执行标记为有效。 |
| `11` | 匹配类型 | 一个整数，其值如下表所示。 | 如果当前状态的类型与参数中指定的类型匹配，则将执行标记为有效；否则，标记为无效。 |

当你使用匹配类型操作（上表中的操作码 11）编写 entitlements `$query` 时，使用下表中的值之一作为参数：

| 值 | 上下文的期望类型 |
|---|---|
| 1 | 一个字典 |
| 2 | 一个数组 |
| 3 | 一个整数 |
| 4 | 一个字符串 |
| 5 | 一个布尔值 |

下面示例中的启动约束使用 `entitlements` 事实和 `$query` 操作符，要求可执行文件具有 [Camera entitlement](../bundleresources/entitlements/com.apple.security.device.camera.md)（`com.apple.security.device.camera`），且其布尔值为 `true`。

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>entitlements</key>
  <dict>
    <key>$query</key>
    <array>
      <array>
        <integer>1</integer>
        <string>com.apple.security.device.camera</string>
      </array>
      <array>
        <integer>5</integer>
        <true/>
      </array>
    </array>
  </dict>
</dict>
</plist>
```
