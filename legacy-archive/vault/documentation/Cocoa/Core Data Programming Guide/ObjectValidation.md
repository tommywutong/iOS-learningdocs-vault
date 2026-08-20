---
title: Core Data 编程指南
apple_id: TP40001075
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: CoreData
published: '2017-03-27'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreData/ObjectValidation.html
archived_at: '2026-07-15T07:14:25.826137Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Core Data 编程指南](index.md)



## 对象校验

Cocoa 为模型值校验提供了一套基础设施，但它要求你为想要施加的每一条约束编写代码。相比之下，Core Data 允许你将校验逻辑放入托管对象模型中，并将大多数常见约束直接以声明的方式指定，而不必在代码中编写校验逻辑。你可以为数值属性和日期属性指定最大值和最小值，为字符串属性指定最大长度和最小长度，以及字符串属性必须匹配的正则表达式。你还可以为关系指定约束，例如将其设为必填，或限制其数量不能超过某个上限。

如果你确实需要自定义单个 property 的校验，可以使用 `NSKeyValueCoding` 协议定义的标准校验方法，具体请参见 [实现自定义的属性级校验](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanzvfvbuqmrqfvjvona)。要校验多个值的组合（例如数组）以及关系，请参见 [实现自定义的跨属性校验](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanzvfvbuqmrqfvjvoni)。

### Core Data 中校验的工作方式

如何校验是一个模型层面的决定，_何时_校验则是用户界面或控制器层面的决定。例如，某个文本字段的值绑定可能启用了"立即校验"（validates immediately）选项。此外，在各种时刻，托管对象和对象图中出现不一致的状态都是预料之中的。

一个内存中的对象可能会暂时处于不一致状态。Core Data 只会在保存操作期间或在被显式请求时应用校验约束（你也可以在应用程序流程中任何合适的时机直接调用校验方法）。有时，在更改一发生就立即进行校验并报告错误会很有用；而在另一些情况下，等到一个工作单元完成后再进行校验才更合理。如果要求托管对象必须始终处于有效状态，这将（除其他影响外）强制用户遵循某种特定的工作流程。允许在托管对象处于无效状态时仍能操作它，也正是托管对象上下文作为"草稿纸"（scratch pad）这一理念的基础——通常你可以将托管对象带到这张草稿纸上，随意编辑，最终再提交更改或将其丢弃。

### 实现自定义的属性级校验

`NSKeyValueCoding` 协议定义了 [validateValue:forKey:error:](https://developer.apple.com/documentation/objectivec/nsobject/1416754-validatevalue) 方法，用来为校验方法提供通用支持，其方式与 [valueForKey:](https://developer.apple.com/documentation/coredata/nsmanagedobject/1506613-value) 为存取方法提供支持的方式类似。

[NSManagedObject](https://developer.apple.com/documentation/coredata/nsmanagedobject) 为实现属性（及跨属性）值的校验提供了统一的钩子。如果你想在托管对象模型已提供的约束之外再实现额外的逻辑，不要重写 `validateValue:forKey:error:`，而应实现形如 `validate<Key>:error:` 的方法。如果你实现了自定义的校验方法，通常不应直接调用它们，而应以相应的键调用通用方法 `validateValue:forKey:error:`。这样可以确保托管对象模型中定义的约束也会一并被应用。如果你转而直接调用 `validate<Key>: error:`，模型中的约束可能不会被应用。

在方法实现中，你需要检查提议的新值，如果它不满足你的约束，就返回 `NO``false`。如果 error 参数不为 `null`，你还需要创建一个描述问题的 [NSError](https://developer.apple.com/documentation/foundation/nserror) 对象，如下例所示。该示例校验 age 值是否大于零，如果不是，则返回一个错误。

Objective-C

1. `- (BOOL)validateAge:(id*)ioValue error:(NSError**)outError`
2. `{`
3. `if (*ioValue == nil) {`
4. `return YES;`
5. `}`
6. `if ([*ioValue floatValue] <= 0.0) {`
7. `if (outError == NULL) {`
8. `return NO;`
9. `}`
10. `NSString *errorStr = NSLocalizedStringFromTable(@"Age must be greater than zero", @"Employee", @"validation: zero age error");`
11. `NSDictionary *userInfoDict = @{NSLocalizedDescriptionKey: errorStr};`
12. `NSError *error = [[NSError alloc] initWithDomain:EMPLOYEE_ERROR_DOMAIN code:PERSON_INVALID_AGE_CODE userInfo:userInfoDict];`
13. `*outError = error;`
14. `return NO;`
15. `} else {`
16. `return YES;`
17. `}`
18. `}`

Swift

1. `func validateAge(value: AutoreleasingUnsafeMutablePointer<AnyObject?>) throws {`
2. `if value == nil {`
3. `return`
4. `}`
6. `let valueNumber = value?.pointee as! NSNumber`
7. `if valueNumber.floatValue > 0.0 {`
8. `return`
9. `}`
10. `let errorStr = NSLocalizedString("Age must be greater than zero", tableName: "Employee", comment: "validation: zero age error")`
11. `let userInfoDict = [NSLocalizedDescriptionKey: errorStr]`
12. `let error = NSError(domain: "EMPLOYEE_ERROR_DOMAIN", code: 1123, userInfo: userInfoDict)`
13. `throw error`
14. `}`

输入值是一个指向对象引用的指针（一个 `id *`）。这意味着原则上你可以更改输入值。但强烈不建议这样做，因为这可能带来严重的内存管理问题（参见 _[Key-Value Coding Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/index.html#//apple_ref/doc/uid/10000107i)_ 中的 [Key-Value Validation](../Key-Value%20Coding%20Programming%20Guide/Validation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsge3tg)）。此外，不要在自定义 property 校验方法内部调用 `validateValue:forKey:error:`。如果你这样做，当 `validateValue:forKey:error:` 在运行时被调用时，就会产生无限循环。

除非值是无效的或未经强制转换的，否则不要在 `validate<Key>:error:` 方法中更改输入值。原因是，因为对象和上下文现在已经变脏（dirty），Core Data 之后可能会再次校验该键。如果你在校验方法中持续执行强制转换，就可能产生无限循环。类似地，如果你实现了会产生变更或副作用的校验方法和 [willSave](https://developer.apple.com/documentation/coredata/nsmanagedobject/1506209-willsave) 方法，也要格外小心——Core Data 会持续重新校验这些更改，直到达到稳定状态为止。

### 实现自定义的跨属性校验

一个对象的所有单个 attribute 的值都可能各自有效，但这些值的组合却可能无效。例如，考虑一个存储人员年龄以及是否持有驾照的应用程序。对于一个 Person 对象，`12` 可能是 `age` attribute 的一个有效值，`YES`/`true` 也是 `hasDrivingLicense` attribute 的一个有效值，但（至少在大多数国家）这种值的组合是无效的。

[NSManagedObject](https://developer.apple.com/documentation/coredata/nsmanagedobject) 通过诸如 [validateForUpdate:](https://developer.apple.com/documentation/coredata/nsmanagedobject/1506998-validateforupdate) 这样的 `validateFor…` 方法，为更新、插入和删除提供了额外的校验时机。如果你实现自定义的跨属性校验方法，应先调用父类的实现，以确保单个 property 的校验方法也会被调用。如果父类的实现失败（即存在无效的 attribute 值），你可以执行以下操作之一：

- 返回 `NO`/`false` 以及父类实现所创建的错误。
- 继续执行校验，检查是否存在不一致的值组合。

如果你继续执行校验，请确保你在逻辑中使用的任何值本身不是无效的，以免你的代码本身引发错误。例如，假设你在计算中把某个值为 0 的 attribute 用作除数，但该 attribute 本应要求大于 0。此外，如果你发现了更多校验错误，必须按照 [合并校验错误](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanzvfvbuqmrqfvjvony) 中所述的方式，将它们与已有错误合并，返回一个"多重错误"（multiple errors error）。

以下示例展示了一个 Person 实体的跨属性校验方法实现，该实体拥有两个 attribute：`birthday` 和 `hasDrivingLicense`。约束条件是未满 16 岁的人不能持有驾照。这一约束会同时在 [validateForInsert:](https://developer.apple.com/documentation/coredata/nsmanagedobject/1506683-validateforinsert) 和 [validateForUpdate:](https://developer.apple.com/documentation/coredata/nsmanagedobject/1506998-validateforupdate) 中检查，因此校验逻辑本身被拆分到了一个单独的方法中。

__清单 14-1__Interproperty validation for a Person entity

Objective-C

1. `- (BOOL)validateForInsert:(NSError **)error`
2. `{`
3. `BOOL propertiesValid = [super validateForInsert:error];`
4. `// could stop here if invalid`
5. `BOOL consistencyValid = [self validateConsistency:error];`
6. `return (propertiesValid && consistencyValid);`
7. `}`
8. `- (BOOL)validateForUpdate:(NSError **)error`
9. `{`
10. `BOOL propertiesValid = [super validateForUpdate:error];`
11. `// could stop here if invalid`
12. `BOOL consistencyValid = [self validateConsistency:error];`
13. `return (propertiesValid && consistencyValid);`
14. `}`
15. `- (BOOL)validateConsistency:(NSError **)error`
16. `{`
17. `static NSCalendar *gregorianCalendar;`
18. `NSDate *myBirthday = [self birthday];`
19. `if (myBirthday == nil) {`
20. `return YES;`
21. `}`
22. `if ([[self hasDrivingLicense] boolValue] == NO) {`
23. `return YES;`
24. `}`
25. `if (gregorianCalendar == nil) {`
26. `gregorianCalendar = [[NSCalendar alloc] initWithCalendarIdentifier:NSCalendarIdentifierGregorian];`
27. `}`
28. `NSDateComponents *components = [gregorianCalendar components:NSCalendarUnitYear fromDate:myBirthday toDate:[NSDate date] options:0];`
29. `NSInteger years = [components year];`
30. `if (years >= 16) {`
31. `return YES;`
32. `}`
33. `if (error == NULL) {`
34. `//don't create an error if none was requested`
35. `return NO;`
36. `}`
37. `NSBundle *myBundle = [NSBundle bundleForClass:[self class]];`
38. `NSString *drivingAgeErrorString = [myBundle localizedStringForKey:@"TooYoungToDriveError" value:@"Person is too young to have a driving license." table:@"PersonErrorStrings"];`
39. `NSMutableDictionary *userInfo = [NSMutableDictionary dictionary];`
40. `[userInfo setObject:drivingAgeErrorString forKey:NSLocalizedFailureReasonErrorKey];`
41. `[userInfo setObject:self forKey:NSValidationObjectErrorKey];`
42. `NSError *drivingAgeError = [NSError errorWithDomain:EMPLOYEE_ERROR_DOMAIN code:NSManagedObjectValidationError userInfo:userInfo];`
43. `if (*error == nil) { // if there was no previous error, return the new error`
44. `*error = drivingAgeError;`
45. `} else { // if there was a previous error, combine it with the existing one`
46. `*error = [self errorFromOriginalError:*error error:drivingAgeError];`
47. `}`
48. `return NO;`
49. `}`

Swift

1. `override func validateForInsert() throws {`
2. `try super.validateForInsert()`
3. `try validateConsistency()`
4. `}`
5. `override func validateForUpdate() throws {`
6. `try super.validateForUpdate()`
7. `try validateConsistency()`
8. `}`
9. `func validateConsistency() throws {`
10. `guard let myBirthday = dateOfBirth as? Date else {`
11. `let errString = "Person has no birth date set."`
12. `let userInfo = [NSLocalizedFailureReasonErrorKey: errString, NSValidationObjectErrorKey: self] as [String : Any]`
13. `throw NSError(domain: "EMPLOYEE_ERROR_DOMAIN", code: 1124, userInfo: userInfo)`
14. `}`
15. `if !hasDrivingLicense {`
16. `return`
17. `}`
19. `let gregorianCalendar = NSCalendar(calendarIdentifier: NSCalendarIdentifierGregorian)!`
21. `let components = gregorianCalendar.components(.Year, fromDate: myBirthday, toDate: Date(), options:.WrapComponents)`
22. `if components.year >= 16 {`
23. `return`
24. `}`
26. `let errString = "Person is too young to have a driving license."`
27. `let userInfo = [NSLocalizedFailureReasonErrorKey: errString, NSValidationObjectErrorKey: self]`
28. `let error = NSError(domain: "EMPLOYEE_ERROR_DOMAIN", code: 1123, userInfo: userInfo)`
29. `throw error`
30. `}`

### 合并校验错误

如果在单次操作中出现多个校验失败，你需要创建并返回一个错误码为 [NSValidationMultipleErrorsError](https://developer.apple.com/documentation/coredata/1535452-validation_error_codes/nsvalidationmultipleerrorserror)（表示多重错误）的 [NSError](https://developer.apple.com/documentation/foundation/nserror) 对象。你需要将各个独立的错误添加到一个数组中，再使用键 [NSDetailedErrorsKey](https://developer.apple.com/documentation/coredata/nsdetailederrorskey) 将该数组添加到 `NSError` 对象的 user info 字典中。这一模式同样适用于父类校验方法返回的错误。根据你所执行的测试数量，定义一个方法来将已有的 `NSError` 对象（它本身也可能是一个多重错误）与一个新错误合并、并返回一个新的多重错误，可能会比较方便。

以下示例展示了一个简单方法的实现，用于将两个错误合并为单个多重错误。具体如何合并取决于原始错误本身是否已经是一个多重错误：如果原始错误已经是多重错误，则将第二个错误添加进去；否则，将两个错误组合起来创建一个新的多重错误。

> [!NOTE]
> 

__清单 14-2__将两个错误合并为单个多重错误的方法

Objective-C

1. `- (NSError *)errorFromOriginalError:(NSError *)originalError error:(NSError*)secondError`
2. `{`
3. `NSMutableDictionary *userInfo = [NSMutableDictionary dictionary];`
4. `NSMutableArray *errors = [NSMutableArray arrayWithObject:secondError];`
5. `if ([originalError code] == NSValidationMultipleErrorsError) {`
6. `[userInfo addEntriesFromDictionary:[originalError userInfo]];`
7. `[errors addObjectsFromArray:[userInfo objectForKey:NSDetailedErrorsKey]];`
8. `} else {`
9. `[errors addObject:originalError];`
10. `}`
11. `[userInfo setObject:errors forKey:NSDetailedErrorsKey];`
12. `return [NSError errorWithDomain:NSCocoaErrorDomain code:NSValidationMultipleErrorsError userInfo:userInfo];`
13. `}`

Swift

1. `func errorFromOriginalError(_ originalError: NSError, secondError: NSError) -> NSError {`
2. `var userInfo = [String : Any]()`
3. `var errors = [NSError]()`
4. `if originalError.code == NSValidationMultipleErrorsError {`
5. `for (k, v) in originalError.userInfo {`
6. `guard let key = k as? String else { continue }`
7. `userInfo.updateValue(v as AnyObject, forKey: key)`
8. `}`
9. `if let detailedErrors = userInfo[NSDetailedErrorsKey] as? [NSError] {`
10. `errors = errors + detailedErrors`
11. `}`
12. `} else {`
13. `errors.append(originalError)`
14. `}`
15. `userInfo[NSDetailedErrorsKey] = errors`
16. `return NSError(domain: NSCocoaErrorDomain, code: NSValidationMultipleErrorsError, userInfo: userInfo)`
17. `}`

[Faulting and Uniquing](FaultingandUniquing.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanzvfvbuqmjyfvjvomi)

[Change Management](ChangeManagement.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanzvfvbuqmrsfvjvomi)
