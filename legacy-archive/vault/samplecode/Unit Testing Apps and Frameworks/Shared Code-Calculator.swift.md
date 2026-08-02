---
title: Unit Testing Apps and Frameworks
apple_id: DTS40011742
resource_type: Sample Code
platform: iOS|macOS
topic: Xcode
technology: null
published: '2018-04-26'
source_url: https://developer.apple.com/library/archive/samplecode/UnitTests/Listings/Shared_Code_Calculator_swift.html
archived_at: '2026-07-18T03:27:34.332744Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Unit Testing Apps and Frameworks](Unit%20Testing%20Apps%20and%20Frameworks.md)


[Next](Shared%20Code-CalculatorError.swift.md)[Previous](Shared%20Code-CalculatorKitExtensions.swift.md)

# Shared Code/Calculator.swift

```swift
/*
    Copyright (C) 2018 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Implements the logic for a calculator. Performs the addition, substraction, division,
                and multiplication operations.
*/

import Foundation

open class Calculator {
    // MARK: - Properties

    fileprivate let period = "."
    fileprivate var display: String
    fileprivate var leftOperand: Double?
    fileprivate var operatorValue: String?
    fileprivate var isLastCharacterOperator = false

    /// - returns: The display value of the calculator.
    public var displayValue: String {
        get {
            return !(display.isEmpty) ? display : "0"
        }
    }

    // MARK: - Initialization

    public init() {
        self.display = String()
        self.operatorValue = nil
    }

    // MARK: - Calculator Operation

     /**
        It takes an inputted character, then checks whether it is a number between 0 and 9, an operator (+, -, *, /),
        "D", "C", "=", or a period. Calls the operation function to perform the appropriate calculation.
    */
    public func input(_ input: String?) throws {
        /*
            We must first check that the inputted character is a number between 0 and 9, an operator (+, -, *, /),
            "D", "C", "=", or a period before we can proceed.
        */
        guard let input = input else {
            throw CalculatorError.nilInput
        }

        guard input.isValidCharacter else {
            throw CalculatorError.invalidCharater
        }

        guard input.count == 1 else {
            throw CalculatorError.multipleCharacters
        }

        // If the inputted character is a number (between 0 and 9) or a period, update the display.
        if input.isValidDigit {

            if isLastCharacterOperator {
                display = input
                isLastCharacterOperator = false
            } else if !input.isPeriod || !(display.contains(period)) {
                // Add it to the current display.
                display += input
            }
        /*
             If the inputted character is an operator, save it in operatorValue and the current displayed value in leftOperand.
             If the inputted character is an equal sign, call the operation function to perform a calculation
             using leftOperand, the current displayed value, and operatorValue, then save the result in the display variable.
        */
        } else if input.isOperator || input.isEqualSign {

            if (operatorValue == nil) && !(input.isEqualSign) {
                leftOperand = Double(displayValue)
                operatorValue = input
            } else {
                if let sign = operatorValue, let operand = leftOperand, let rightOperand = Double(displayValue) {

                    if let result = operation(left: operand, right: rightOperand, sign: sign) {
                        // Update the display with the operation's result.
                        display = "\(String(format: "%g", result))"
                    }
                }
                operatorValue = (input.isEqualSign) ? nil : input
            }

            isLastCharacterOperator = true
        // if the inputted character is "C" and there is something displayed, clear it. Clear the saved operator, otherwise.
        } else if input.isClear {
            if !(display.isEmpty) {
                display.removeAll()
            } else {
                operatorValue = nil
            }
        // If the inputted character is "D" and there is something displayed, remove its last character.
        } else if input.isDelete {
            if !display.isEmpty {
                display = String(display.dropLast())
            }
            isLastCharacterOperator = false
        }
    }

    /// - returns: Result of an arithmetic operation using the provided operands and operator.
    fileprivate func operation (left: Double, right: Double, sign: String) -> Double? {
        switch sign {
        case "+": return left + right
        case "-": return left - right
        case "*": return left * right
        case "/": return left / right
        default: break
        }
        return nil
    }
}
```

[Next](Shared%20Code-CalculatorError.swift.md)[Previous](Shared%20Code-CalculatorKitExtensions.swift.md)

