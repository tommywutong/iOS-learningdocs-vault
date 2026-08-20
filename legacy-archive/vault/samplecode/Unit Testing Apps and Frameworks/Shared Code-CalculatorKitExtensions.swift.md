---
title: Unit Testing Apps and Frameworks
apple_id: DTS40011742
resource_type: Sample Code
platform: iOS|macOS
topic: Xcode
technology: null
published: '2018-04-26'
source_url: https://developer.apple.com/library/archive/samplecode/UnitTests/Listings/Shared_Code_CalculatorKitExtensions_swift.html
archived_at: '2026-07-18T03:27:34.211649Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Unit Testing Apps and Frameworks](Unit%20Testing%20Apps%20and%20Frameworks.md)


[Next](Shared%20Code-Calculator.swift.md)[Previous](Shared%20Code-CalculatorKitTests.swift.md)

# Shared Code/CalculatorKitExtensions.swift

```swift
/*
    Copyright (C) 2018 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Creates an extension for the String class.
*/

import Foundation

extension String {

    /// Determines whether the string is the Delete charater.
    var isDelete: Bool {
        return (self == "D")
    }

    /// Determines whether the string is a period.
    var isPeriod: Bool {
        return (self == ".")
    }

    /// Determines whether the string is the Clear charater.
    var isClear: Bool {
        return (self == "C")
    }

    /// Determines whether the string is a period or a number between 0 and 9.
    var isValidDigit: Bool {
        let digits = "0123456789."
        return digits.contains(self)
    }

    /// Determines whether the string is an operator such as +, -, *, or /.
    var isOperator: Bool {
        let operators = "+-*/"
        return operators.contains(self)
    }

    /// Determines whether the string is an equal sign.
    var isEqualSign: Bool {
        return (self == "=")
    }

    /// Determines whether a string is a valid character such as a digit, a.
    var isValidCharacter: Bool {
        return ( isValidDigit || isOperator || isDelete || isClear || isPeriod || isEqualSign)
    }
}
```

[Next](Shared%20Code-Calculator.swift.md)[Previous](Shared%20Code-CalculatorKitTests.swift.md)

