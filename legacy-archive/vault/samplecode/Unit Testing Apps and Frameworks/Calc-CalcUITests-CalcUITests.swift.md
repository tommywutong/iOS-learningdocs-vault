---
title: Unit Testing Apps and Frameworks
apple_id: DTS40011742
resource_type: Sample Code
platform: iOS|macOS
topic: Xcode
technology: null
published: '2018-04-26'
source_url: https://developer.apple.com/library/archive/samplecode/UnitTests/Listings/Calc_CalcUITests_CalcUITests_swift.html
archived_at: '2026-07-18T03:27:33.735583Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Unit Testing Apps and Frameworks](Unit%20Testing%20Apps%20and%20Frameworks.md)


[Next](Calc-Calc-AppDelegate.swift.md)[Previous](Calc%20%28macOS%29-Calc-CalcViewController.swift.md)

# Calc/CalcUITests/CalcUITests.swift

```swift
/*
 Copyright (C) 2018 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Performs UI testing for the Calc app.
 */

import XCTest

class CalcUITests: XCTestCase {
    let app = XCUIApplication()

    // MARK: - Setup and Teardown

    override func setUp() {
        super.setUp()
        // In UI tests it is usually best to stop immediately when a failure occurs.
        continueAfterFailure = false
        // UI tests must launch the application that they test. Doing this in setup will make sure it happens for each test method.
        XCUIApplication().launch()
    }

    override func tearDown() {
        // Put teardown code here. This method is called after the invocation of each test method in the class.
        super.tearDown()
    }

    // MARK: - Addition

    /**
        Performs a chained addition test. The test has two parts:
        1. Enter in the calculator and check: 6 + 2 = 8.
        2. Check: display value + 2 = 10.
    */
    func testAddition() {
        app.buttons["6"].tap()
        app.buttons["+"].tap()
        app.buttons["2"].tap()
        app.buttons["="].tap()

        // Check whether the display textfield shows 8.
        if let textFieldValue = app.textFields["display"].value as? String {
            XCTAssertTrue(textFieldValue == "8", "Part 1 failed.")
        }

        app.buttons["+"].tap()
        app.buttons["2"].tap()
        app.buttons["="].tap()

        // Check whether the display textfield shows 10.
        if let textFieldValue = app.textFields["display"].value as? String {
            XCTAssertTrue(textFieldValue == "10", "Part 2 failed.")
        }
    }

    // MARK: - Subtraction

    /// Performs a substraction test. Enter in the calculator and check: 6 - 2 = 4.
    func testSubtraction() {
        app.buttons["6"].tap()
        app.buttons["-"].tap()
        app.buttons["2"].tap()
        app.buttons["="].tap()

        // Check that whether the display textfield shows 4.
        if let textFieldValue = app.textFields["display"].value as? String {
            XCTAssertTrue(textFieldValue == "4", "Incorrect value.")
        }
    }

    // MARK: - Division

    /// Performs a division test. Enter in the calculator and check: 25 / 4 = 6.25.
    func testDivision() {
        app.buttons["2"].tap()
        app.buttons["5"].tap()
        app.buttons["/"].tap()
        app.buttons["4"].tap()
        app.buttons["="].tap()

        // Check whether the display textfield shows 6.25.
        if let textFieldValue = app.textFields["display"].value as? String {
            XCTAssertTrue(textFieldValue == "6.25", "Incorrect value.")
        }
    }

    // MARK: - Multiplication

    /// Performs a multiplication test. Enter in the calculator and check: 19 x 8 = 152.
    func testMultiplication() {
        app.buttons["1"].tap()
        app.buttons["9"].tap()
        app.buttons["*"].tap()
        app.buttons["8"].tap()
        app.buttons["="].tap()

        // Check whether the display textfield shows 152.
        if let textFieldValue = app.textFields["display"].value as? String {
            XCTAssertTrue(textFieldValue == "152", "Incorrect value.")
        }
    }

    // MARK: - Delete
    /**
        Tests the functionality of the D (Delete) key.
        1. Enter the number 1987 into the calculator.
        2. Delete each digit, and test the display to ensure
           the correct display contains the expected value after each D tap.
    */
    func testDelete() {
        app.buttons["1"].tap()
        app.buttons["9"].tap()
        app.buttons["8"].tap()
        app.buttons["7"].tap()
        app.buttons["="].tap()

        if let textFieldValue = app.textFields["display"].value as? String {
            XCTAssertTrue(textFieldValue == "1987", "Part 1 failed.")
        }

        app.buttons["D"].tap()
        if let textFieldValue = app.textFields["display"].value as? String {
            XCTAssertTrue(textFieldValue == "198", "Part 2 failed.")
        }

        app.buttons["D"].tap()
        if let textFieldValue = app.textFields["display"].value as? String {
            XCTAssertTrue(textFieldValue == "19", "Part 3 failed.")
        }

        app.buttons["D"].tap()

        if let textFieldValue = app.textFields["display"].value as? String {
            XCTAssertTrue(textFieldValue == "1", "Part 4 failed.")
        }

        app.buttons["D"].tap()
        if let textFieldValue = app.textFields["display"].value as? String {
            XCTAssertTrue(textFieldValue == "0", "Part 5 failed.")
        }
    }

    // MARK: - Clear

    /**
        Tests the functionality of the C (Clear) key.
        1. Clear the display.
            - Enter the calculation 25 / 4.
            - Tap C.
            - Ensure the display contains the value 0.
        2. Perform corrected computation.
            - Tap 5, =.
            - Ensure the display contains the value 5.
        3. Ensure tapping C twice clears all.
            - Enter the calculation 19 x 8.
            - Tap C (clears the display).
            - Tap C (clears the operand).
            - Tap +, 2, =.
       - Ensure the display contains the value 2.
    */
    func testClear() {
        app.buttons["2"].tap()
        app.buttons["5"].tap()
        app.buttons["/"].tap()
        app.buttons["4"].tap()
        app.buttons["="].tap()
        app.buttons["C"].tap()
        if let textFieldValue = app.textFields["display"].value as? String {
            XCTAssertTrue(textFieldValue == "0", "Part 1 failed.")
        }

        app.buttons["5"].tap()
        app.buttons["="].tap()
        if let textFieldValue = app.textFields["display"].value as? String {
            XCTAssertTrue(textFieldValue == "5", "Part 2 failed.")
        }

        app.buttons["1"].tap()
        app.buttons["9"].tap()
        app.buttons["*"].tap()
        app.buttons["8"].tap()
        app.buttons["C"].tap()
        app.buttons["C"].tap()
        app.buttons["+"].tap()
        app.buttons["2"].tap()
        app.buttons["="].tap()
        if let textFieldValue = app.textFields["display"].value as? String {
            XCTAssertTrue(textFieldValue == "2", "Part 3 failed.")
        }
    }
}
```

[Next](Calc-Calc-AppDelegate.swift.md)[Previous](Calc%20%28macOS%29-Calc-CalcViewController.swift.md)

