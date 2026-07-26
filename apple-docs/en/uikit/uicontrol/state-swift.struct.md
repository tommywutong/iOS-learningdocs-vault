---
title: UIControl.State
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicontrol/state-swift.struct
source_url: 'https://developer.apple.com/documentation/uikit/uicontrol/state-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicontrol/state-swift.struct.json'
content_hash: 'sha256:b9d3c1fb3ac57d1d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIControl](../uicontrol.md)

# UIControl.State

<sub>Structure</sub>

Constants describing the state of a control.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
struct State
```

## Overview

A control can have more than one state at a time. Controls can have different configurations according to their state. For example, a [UIButton](../uibutton.md) object can display one image when it’s in its normal state and a different image when it’s highlighted.

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [ExpressibleByArrayLiteral](../../swift/expressiblebyarrayliteral.md), [OptionSet](../../swift/optionset.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [SetAlgebra](../../swift/setalgebra.md)

## Topics

### Constants

- [UIControlStateNormal](state-swift.struct/normal.md) — The normal, or default, state of a control where the control is enabled but neither selected nor highlighted.
- [UIControlStateHighlighted](state-swift.struct/highlighted.md) — The highlighted state of a control.
- [UIControlStateDisabled](state-swift.struct/disabled.md) — The disabled state of a control.
- [UIControlStateSelected](state-swift.struct/selected.md) — The selected state of a control.
- [UIControlStateFocused](state-swift.struct/focused.md) — The focused state of a control.
- [UIControlStateApplication](state-swift.struct/application.md) — Additional control-state flags available for app use.
- [UIControlStateReserved](state-swift.struct/reserved.md) — Control-state flags reserved for internal framework use.

### Initializers

- [init(rawValue:)](<state-swift.struct/init(rawvalue_).md>) — Creates a control state with the specified raw value.

## See Also

### Managing state

- [state](state-swift.property.md) — The state of the control, specified as a bit mask value.
- [enabled](isenabled.md) — A Boolean value indicating whether the control is in the enabled state.
- [selected](isselected.md) — A Boolean value indicating whether the control is in the selected state.
- [highlighted](ishighlighted.md) — A Boolean value indicating whether the control draws a highlight.
