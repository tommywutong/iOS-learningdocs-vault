---
title: Unit Testing Apps and Frameworks
apple_id: DTS40011742
resource_type: Sample Code
platform: iOS|macOS
topic: Xcode
technology: null
published: '2018-04-26'
source_url: https://developer.apple.com/library/archive/samplecode/UnitTests/Listings/Shared_Code_CalculatorError_swift.html
archived_at: '2026-07-18T03:27:34.171031Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Unit Testing Apps and Frameworks](Unit%20Testing%20Apps%20and%20Frameworks.md)


[Next](Calc%20%28macOS%29-CalcUITests-CalcUITests.swift.md)[Previous](Shared%20Code-Calculator.swift.md)

# Shared Code/CalculatorError.swift

```swift
/*
 Copyright (C) 2018 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Type used to represent error value thrown for invalid Calculator input.
*/

import Foundation

public enum CalculatorError: Error {
    case invalidCharater
    case multipleCharacters
    case nilInput
}

extension CalculatorError: LocalizedError {

    public var errorDescription: String? {
        switch self {
        case .invalidCharater: return NSLocalizedString("Invalid character exception.", comment: "The input is not a number between 0-9, an operator (+, -, *, /), D, C, =, or a period.")
        case .multipleCharacters: return NSLocalizedString("Multiple characters exception.", comment: "The input contains more than one character.")
        case .nilInput: return NSLocalizedString("Nil exception.", comment: "The input is nil.")
        }
    }
}
```

[Next](Calc%20%28macOS%29-CalcUITests-CalcUITests.swift.md)[Previous](Shared%20Code-Calculator.swift.md)

