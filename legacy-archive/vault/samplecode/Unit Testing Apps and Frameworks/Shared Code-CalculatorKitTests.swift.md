---
title: Unit Testing Apps and Frameworks
apple_id: DTS40011742
resource_type: Sample Code
platform: iOS|macOS
topic: Xcode
technology: null
published: '2018-04-26'
source_url: https://developer.apple.com/library/archive/samplecode/UnitTests/Listings/Shared_Code_CalculatorKitTests_swift.html
archived_at: '2026-07-18T03:27:34.262946Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Unit Testing Apps and Frameworks](Unit%20Testing%20Apps%20and%20Frameworks.md)


[Next](Shared%20Code-CalculatorKitExtensions.swift.md)[Previous](Unit%20Testing%20Apps%20and%20Frameworks.md)

# Shared Code/CalculatorKitTests.swift

```swift
/*
 Copyright (C) 2018 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Unit tests for the CalculatorKit framework.
 */

import XCTest
@testable import CalculatorKit

class CalculatorKitTests: XCTestCase {
    // MARK: - Properties

    var calculator: Calculator?

    // MARK: - Setup and Teardown

    override func setUp() {
        super.setUp()
        // Put setup code here. This method is called before the invocation of each test method in the class.
        calculator = Calculator()
        XCTAssertNotNil(calculator, "Cannot create Calculator instance.")
    }

    override func tearDown() {
        // Put teardown code here. This method is called after the invocation of each test method in the class.
        super.tearDown()
    }

    // MARK: - Addition

    /// Performs a simple addition test: 6 + 2 = 8.
    func testAddition() {
        if let calculator = calculator {
            try? calculator.input("6")
            try? calculator.input("+")
            try? calculator.input("2")
            try? calculator.input("=")
            XCTAssertTrue(calculator.displayValue == "8")
        }
    }

    // MARK: - Subtraction

    /// Performs a simple subtraction test: 19 - 2 = 17.
    func testSubtraction() {
        if let calculator = calculator {
            try? calculator.input("1")
            try? calculator.input("9")
            try? calculator.input("-")
            try? calculator.input("2")
            try? calculator.input("=")
            XCTAssertTrue(calculator.displayValue == "17")
        }
    }

    // MARK: - Division

    /// Performs a simple division test: 19 / 8 = 2.375.
    func testDivision() {
        if let calculator = calculator {
            try? calculator.input("1")
            try? calculator.input("9")
            try? calculator.input("/")
            try? calculator.input("8")
            try? calculator.input("=")
            XCTAssertTrue(calculator.displayValue == "2.375")
        }
    }

    // MARK: - Multiplication

    /// Performs a simple multiplication test: 6 * 2 = 12.
    func testMultiplication() {
        if let calculator = calculator {
            try? calculator.input("6")
            try? calculator.input("*")
            try? calculator.input("2")
            try? calculator.input("=")
            XCTAssertTrue(calculator.displayValue == "12")
        }
    }

    // MARK: - Subtraction Negative Result

    /// Performs a simple subtraction test with a negative result: 6 - 24 = -18.
    func testSubtractionNegativeResult() {
        if let calculator = calculator {
            try? calculator.input("6")
            try? calculator.input("-")
            try? calculator.input("2")
            try? calculator.input("4")
            try? calculator.input("=")
            XCTAssertTrue(calculator.displayValue == "-18")
        }
    }

    // MARK: - Clear Last Entry

    /// Tests that the clear (C) key clears the last entry when used once.
    func testClearLastEntry() {
        if let calculator = calculator {
            try? calculator.input("7")
            try? calculator.input("+")
            try? calculator.input("3")
            try? calculator.input("C")
            try? calculator.input("4")
            try? calculator.input("=")
            XCTAssertTrue(calculator.displayValue == "11")
        }
    }

    // MARK: - Clear Computation

    /// Tests that the clear (C) key clears the computation when used twice.
    func testClearComputation() {
        if let calculator = calculator {
            try? calculator.input("C")
            try? calculator.input("7")
            try? calculator.input("+")
            try? calculator.input("3")
            try? calculator.input("C")
            try? calculator.input("C")
            XCTAssertTrue(calculator.displayValue == "0")
        }
    }

    // MARK: - Input Exception

    /**
        Tests that the input: method throws an exception in three situations:
        1. The argument contains more than one character.
        2. The argument contains an invalid character.
        3. The argument is nil.
    */
    func testInputException() {
        if let calculator = calculator {
            XCTAssertThrowsError(try calculator.input("67")) { error in
                print(error.localizedDescription)
            }

            XCTAssertThrowsError(try calculator.input("j")) { error in
                print(error.localizedDescription)
            }

            XCTAssertThrowsError(try calculator.input(nil)) { error in
                print(error.localizedDescription)
            }
        }
    }
}
```

[Next](Shared%20Code-CalculatorKitExtensions.swift.md)[Previous](Unit%20Testing%20Apps%20and%20Frameworks.md)

