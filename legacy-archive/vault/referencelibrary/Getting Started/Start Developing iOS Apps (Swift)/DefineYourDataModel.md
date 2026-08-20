---
title: Start Developing iOS Apps (Swift)
apple_id: TP40015214
resource_type: Guide
platform: iOS
topic: General
technology: null
published: '2016-12-08'
source_url: https://developer.apple.com/library/archive/referencelibrary/GettingStarted/DevelopiOSAppsSwift/DefineYourDataModel.html
archived_at: '2026-07-27T06:57:09.860604Z'
---
> 导航：[总目录](../../../README.md) · [referencelibrary](../../../_indexes/referencelibrary.md) · [Start Developing iOS Apps (Swift)](index.md)


[Next](CreateATableView.md)[Previous](ImplementingACustomControl.md)

## Define Your Data Model

In this lesson, you’ll define and test a [data model](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvomzv) for the FoodTracker app. A data model represents the structure of the information stored in an app.

### Learning Objectives

At the end of the lesson, you’ll be able to:

- Create a data model
- Write failable initializers for a custom class
- Demonstrate a conceptual understanding of the difference between failable and nonfailable initializers
- Test a data model by writing and running unit tests

### Create a Data Model

Now you’ll create a data model to store the information that the meal [scene](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvonrs) needs to display. To do so, you define a simple [class](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvomy) with a name, a photo, and a rating.

__To create a new data model class__

1. Choose File > New > File (or press Command-N).
2. At the top of the dialog that appears, select iOS.
3. Select Swift File, and click Next.

   You’re using a different process to create this class than the `RatingControl` class you created earlier (iOS > Source > Cocoa Touch Class), because you’re defining a [base class](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvonzz) for your data model, which means it doesn’t need to inherit from any other classes.
4. In the Save As field, type `Meal`.
5. The save location defaults to your project directory.

   The Group option defaults to your app name, FoodTracker.

   In the Targets section, your app is selected and the tests for your app are unselected.
6. Leave these defaults as they are, and click Create.

   Xcode creates a file called `Meal.swift`. In the Project navigator, drag the `Meal.swift` file and position it under the other Swift files, if necessary.

In Swift, you can represent the name using a `String`, the photo using a `UIImage`, and the rating using an `Int`. Because a meal always has a name and rating but might not have a photo, make the `UIImage` an [optional](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvomjr).

__To define a data model for a meal__

1. If the [assistant editor](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvonzw) is open, return to the standard editor by clicking the Standard button.

   （原归档配图未能恢复：`standard_toggle_2x.png`）
2. Open `Meal.swift`.
3. Change the import statement to import UIKit instead of Foundation:

   1. `import UIKit`

   When Xcode creates a new Swift file, it imports the Foundation framework by default, letting you work with Foundation data structures in your code. You’ll also be working with a class from the UIKit framework, so you need to import UIKit. However, importing UIKit also gives you access to Foundation, so you can remove the redundant import to Foundation.
4. Below the import statement, add the following code:

   1. `class Meal {`
   3. `//MARK: Properties`
   5. `var name: String`
   6. `var photo: UIImage?`
   7. `var rating: Int`
   9. `}`

   This code defines the basic properties for the data you need to store. You’re making these variables (`var`) instead of constants (`let`) because they’ll need to change throughout the course of a `Meal` object’s lifetime.
5. Below the properties, add this code to declare an initializer:

   1. `//MARK: Initialization`
   3. `init(name: String, photo: UIImage?, rating: Int) {`
   5. `}`

   Recall that an [initializer](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvomq) is a method that prepares an instance of a class for use, which involves setting an initial value for each [property](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvonjy) and performing any other setup or initialization.
6. Fill out the basic implementation by setting the properties equal to the parameter values.

   1. `// Initialize stored properties.`
   2. `self.name = name`
   3. `self.photo = photo`
   4. `self.rating = rating`

   But what happens if you try to create a Meal with incorrect values, like an empty name or a negative rating? You’ll need to return [nil](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvoni) to indicate that the item couldn’t be created, and has set to the default values. You need to add code to check for those cases and to return `nil` if they fail.
7. Add the following code just above the code that initializes the stored properties.

   1. `// Initialization should fail if there is no name or if the rating is negative.`
   2. `if name.isEmpty || rating < 0 {`
   3. `return nil`
   4. `}`

   This code validates the incoming parameters and returns `nil` if they contain invalid values.

   Note, the compiler should complain with an error stating, “Only failable initializers can return ‘nil’.”
8. Click the error icon to bring up the fix-it.

   （原归档配图获取待重试：`DYDM_init_fixit_2x.png`）
9. Double-click the fix it to update your initializer. The initializer’s signature should now look like this:

   1. `init?(name: String, photo: UIImage?, rating: Int) {`

   Failable initializers always start with either `init?` or `init!`. These initializers return [optional](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvomjr) values or [implicitly unwrapped optional](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvonjq) values, respectively. Optionals can either contain a valid value or `nil`. You must check to see if the optional has a value, and then safely unwrap the value before you can use it. Implicitly unwrapped optionals are optionals, but the system implicitly unwraps them for you.

   In this case, your initializer returns an optional `Meal?` object.

At this point, your `init?(name: String, photo: UIImage?, rating: Int)` initializer should look like this:

1. `init?(name: String, photo: UIImage?, rating: Int) {`
3. `// Initialization should fail if there is no name or if the rating is negative.`
4. `if name.isEmpty || rating < 0 {`
5. `return nil`
6. `}`
8. `// Initialize stored properties.`
9. `self.name = name`
10. `self.photo = photo`
11. `self.rating = rating`
13. `}`
> [!NOTE]
>
> As you will see in later lessons, failable initializers are harder to use because you need to unwrap the returned optional before using it. Some developers prefer to enforce an initializer’s contract using `assert()` or `precondition()` methods. These methods cause the app to terminate if the condition they are testing fails. This means that the calling code must validate the inputs before calling the initializer.
>
> For more information on initializers, see Initialization. For information on adding inline sanity checks and preconditions to your code, see [assert(_:_:file:line:)](https://developer.apple.com/documentation/swift/1541112-assert) and [precondition(_:_:file:line:)](https://developer.apple.com/documentation/swift/1540960-precondition).

_Checkpoint:_ Build your project by choosing Product > Build (or pressing Command-B). You’re not using your new class for anything yet, but building it gives the compiler a chance to verify that you haven’t made any typing mistakes. If you have, fix them by reading through the warnings or errors that the compiler provides, and then look back over the instructions in this lesson to make sure everything looks the way it’s described here.

### Test Your Data

Although your data model code builds, you haven’t fully incorporated it into your app yet. As a result, it’s hard to tell whether you’ve implemented everything correctly, and if you might encounter edge cases that you haven’t considered at runtime.

To address this uncertainty, you can write unit tests. [Unit tests](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvonzr) are used for testing small, self-contained pieces of code to make sure they behave correctly. The `Meal` class is a perfect candidate for unit testing.

Xcode has already created a unit test file as part of the Single View Application template.

__To look at the unit test file for FoodTracker__

1. Open the FoodTrackerTests folder in the project navigator by clicking the disclosure triangle next to it.

   （原归档配图获取待重试：`DYDM_foodtrackertests_2x.png`）
2. Open `FoodTrackerTests.swift`.

Take a moment to understand the code in the file so far.

1. `import XCTest`
2. `@testable import FoodTracker`
4. `class FoodTrackerTests: XCTestCase {`
6. `override func setUp() {`
7. `super.setUp()`
8. `// Put setup code here. This method is called before the invocation of each test method in the class.`
9. `}`
11. `override func tearDown() {`
12. `// Put teardown code here. This method is called after the invocation of each test method in the class.`
13. `super.tearDown()`
14. `}`
16. `func testExample() {`
17. `// This is an example of a functional test case.`
18. `// Use XCTAssert and related functions to verify your tests produce the correct results.`
19. `}`
21. `func testPerformanceExample() {`
22. `// This is an example of a performance test case.`
23. `self.measure {`
24. `// Put the code you want to measure the time of here.`
25. `}`
26. `}`
28. `}`

The code starts by importing both the XCTest framework and your app.

Note that the code uses the `@testable` attribute when importing your app. This gives your tests access to the internal elements of your app’s code. Remember, Swift defaults to internal access control for all the types, variables, properties, initializers, and functions in your code. If you haven’t explicitly marked an item as file private or private, you can access it from your tests.

The XCTest framework is Xcode’s testing framework. The unit tests themselves are defined in a class, `FoodTrackerTests`, which inherits from `XCTestCase`. The code comments explain the `setUp()` and `tearDown()` methods, as well as the two sample test cases: `testExample()` and `testPerformanceExample()`.

The main types of tests you can write are functional tests (to check that everything is producing the values you expect) and performance tests (to check that your code is performing as fast as you expect it to). Because you haven’t written any performance-heavy code, you’ll only want to write functional tests for now.

Test cases are simply methods that the system automatically runs as part of your unit tests. To create a test case, create a method whose name starts with the word _test_. It’s best to give your test cases descriptive names. These names make it easier to identify individual tests later on. For example, a test that checks the `Meal` class’s initialization code could be named `testMealInitialization`.

__To write a unit test for Meal object initialization__

1. In `FoodTrackerTests.swift`, you don’t need to use any of the template’s stub methods for this lesson. Delete the template’s methods. Your food tracker tests should appear as shown below:

   1. `import XCTest`
   2. `@testable import FoodTracker`
   4. `class FoodTrackerTests: XCTestCase {`
   6. `}`
2. Before the last curly brace (`}`), add the following:

   1. `//MARK: Meal Class Tests`

   This is a comment to help you (and anybody else who reads your code) navigate through your tests and identify what they correspond to.
3. Below the comment, add a new test case:

   1. `// Confirm that the Meal initializer returns a Meal object when passed valid parameters.`
   2. `func testMealInitializationSucceeds() {`
   4. `}`

   The system automatically runs this test case when the unit tests are run.
4. Add tests to the test case that use both no rating and the highest positive rating.

   1. `// Zero rating`
   2. `let zeroRatingMeal = Meal.init(name: "Zero", photo: nil, rating: 0)`
   3. `XCTAssertNotNil(zeroRatingMeal)`
   5. `// Highest positive rating`
   6. `let positiveRatingMeal = Meal.init(name: "Positive", photo: nil, rating: 5)`
   7. `XCTAssertNotNil(positiveRatingMeal)`

   If the initializer is working as expected, these calls to `init(name:, photo:, rating:)` should succeed. `XCTAssertNotNil` verifies this, by checking that the returned `Meal` object is not `nil`.
5. Now add a test case where the `Meal` class’s initialization should fail. Add the following method under the `testMealInitializationSucceeds()` method.

   1. `// Confirm that the Meal initialier returns nil when passed a negative rating or an empty name.`
   2. `func testMealInitializationFails() {`
   4. `}`

   Again, the system automatically runs this test case when the unit tests are run.
6. Now add tests to the test case that calls the initializer with invalid parameters.

   1. `// Negative rating`
   2. `let negativeRatingMeal = Meal.init(name: "Negative", photo: nil, rating: -1)`
   3. `XCTAssertNil(negativeRatingMeal)`
   5. `// Empty String`
   6. `let emptyStringMeal = Meal.init(name: "", photo: nil, rating: 0)`
   7. `XCTAssertNil(emptyStringMeal)`

   If the initializer is working as expected, these calls to `init(name:, photo:, rating:)` should fail. `XCTAssertNil` verifies this by checking that the returned `Meal` object is `nil`.
7. So far, all of the tests should succeed. Now add a test that will fail. Add the following code between the negative rating and the empty string tests:

   1. `// Rating exceeds maximum`
   2. `let largeRatingMeal = Meal.init(name: "Large", photo: nil, rating: 6)`
   3. `XCTAssertNil(largeRatingMeal)`

Your unit test class should look like this:

1. `class FoodTrackerTests: XCTestCase {`

You can add additional `XCTestCase` subclasses to your FoodTrackerTests target to add additional test cases. Run all of your unit tests at the same time by choosing Product > Test (or pressing Command-U). You can also run an individual test.

_Checkpoint_: Run your unit tests by selecting the Product > Test menu item. The `testMealInitializationSucceeds()` test case should succeed, while the `testMealInitializationFails()` test case fails.

Notice that Xcode automatically opens the Test navigator on the left, and highlights the test that failed.

（原归档配图获取待重试：`DYDM_failtest_2x.png`）

The editor window shows the results of the currently open file. In this case, a test case fails if one or more of its test methods fail. A test method fails if one or more of its tests fail. In this example, only the `XCTAssertNil(largeRatingMeal)` test actually failed.

The Test navigator also lists the individual test methods, grouped by test case. Click the test method to navigate to its code in the editor. The icon to the right shows whether the test method succeeded or failed. You can rerun a test method by moving the mouse over the success or failure icon. When it turns into a play arrow icon, click it.

As you see, unit testing helps catch errors in your code. They also help to define your class’s expected behavior. In this case, the Meal class’s initializer fails if you pass an empty string or a negative rating, but doesn’t fail if you pass a rating greater than 5. Go back and fix that.

__To fix the error__

1. In `Meal.swift`, find the `init?(name:, photo:, rating:)` method.
2. You could modify the `if` clause, but complex Boolean expressions get hard to understand. Instead, replace it with a series of checks. Furthermore, because you are validating data before letting code execute, use [guard](GlossaryDefinitions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjsfvjvomjtga) statements.

   A `guard` statement declares a condition that must be true in order for the code after the `guard` statement to be executed. If the condition is `false`, the `guard` statement’s `else` branch must exit the current code block (for example, by calling `return`, `break`, `continue`, `throw`, or a method that doesn’t return like `fatalError(_:file:line:)`).

   Replace this code:

   1. `// Initialization should fail if there is no name or if the rating is negative.`
   2. `if name.isEmpty || rating < 0 {`
   3. `return nil`
   4. `}`

   With the following:

   1. `// The name must not be empty`
   2. `guard !name.isEmpty else {`
   3. `return nil`
   4. `}`
   6. `// The rating must be between 0 and 5 inclusively`
   7. `guard (rating >= 0) && (rating <= 5) else {`
   8. `return nil`
   9. `}`

Your `init?(name:, photo:, rating:)` method should look like this:

1. `init?(name: String, photo: UIImage?, rating: Int) {`
3. `// The name must not be empty`
4. `guard !name.isEmpty else {`
5. `return nil`
6. `}`
8. `// The rating must be between 0 and 5 inclusively`
9. `guard (rating >= 0) && (rating <= 5) else {`
10. `return nil`
11. `}`
13. `// Initialize stored properties.`
14. `self.name = name`
15. `self.photo = photo`
16. `self.rating = rating`
18. `}`

_Checkpoint_: Your app runs with the unit test you just wrote. All test cases should pass.

（原归档配图未能恢复：`DYDM_passtest_2x.png`）

Unit testing is an essential part of writing code because it helps you catch errors that you might otherwise overlook. As implied by their name, it’s important to keep unit tests modular. Each test should check for a specific, basic type of behavior. If you write unit tests that are long or complicated, it’ll be harder to track down exactly what’s going wrong.

### Wrapping Up

In this lesson, you built a model class to hold your app’s data. You also examined the difference between regular initializers and failable initializers. Finally, you added a couple of unit tests to help you find and fix bugs in your code.

In later lessons, you will use model objects in your app’s code to create and manage the list of meals. However, before you do that, you need to learn how to display a list of meals using a table view.

> [!NOTE]
>
> To see the completed sample project for this lesson, download the file and view it in Xcode.
>
> （原归档配图未能恢复：`WWDR_download_icon_withPadding_2x.png`）[Download File](https://developer.apple.com/sample-code/swift/downloads/05_DefineYourDataModel.zip)

[Implement a Custom Control](ImplementingACustomControl.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqmjzfvjvomi)

[Create a Table View](CreateATableView.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqobnknltc)

Copyright © 2018 Apple Inc. All rights reserved.
[Terms of Use](http://www.apple.com/legal/terms/site.html) |
[Privacy Policy](http://www.apple.com/privacy/) |
[Updated: 2016-12-08](RevisionHistory.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temjufvbuqojzfvjvomi)

[Next](CreateATableView.md)[Previous](ImplementingACustomControl.md)
