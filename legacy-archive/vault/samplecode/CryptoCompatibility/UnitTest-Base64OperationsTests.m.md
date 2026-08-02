---
title: CryptoCompatibility
apple_id: DTS40013654
resource_type: Sample Code
platform: iOS|macOS
topic: Security
technology: Security
published: '2016-11-17'
source_url: https://developer.apple.com/library/archive/samplecode/CryptoCompatibility/Listings/UnitTest_Base64OperationsTests_m.html
archived_at: '2026-07-18T03:05:23.335323Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CryptoCompatibility](CryptoCompatibility.md)


[Next](UnitTest-CryptorOperationsTests.m.md)[Previous](UnitTest-KeyDerivationOperationsTests.m.md)

# UnitTest/Base64OperationsTests.m

```objc
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Tests for the Base64 operations.
 */

@import XCTest;

#import "QCCBase64Encode.h"
#import "QCCBase64Decode.h"

#import "ToolCommon.h"

NS_ASSUME_NONNULL_BEGIN

@interface Base64OperationsTests : XCTestCase

@end

NS_ASSUME_NONNULL_END

@implementation Base64OperationsTests

- (void)setUp {
    [super setUp];
    [ToolCommon sharedInstance].debugRunOpOnMainThread = YES;
}

- (void)testBase64Encode {
    NSData *            inputData;
    QCCBase64Encode *   op;
    NSString *          expectedOutputString;

    inputData = [NSData dataWithContentsOfURL:[[NSBundle bundleForClass:[self class]] URLForResource:@"test" withExtension:@"cer"]];
    assert(inputData != nil);

    expectedOutputString = [NSString stringWithContentsOfURL:[[NSBundle bundleForClass:[self class]] URLForResource:@"test" withExtension:@"pem"] encoding:NSUTF8StringEncoding error:NULL];
    assert(expectedOutputString != nil);

    op = [[QCCBase64Encode alloc] initWithInputData:inputData];
    op.addLineBreaks = YES;
    [[ToolCommon sharedInstance] synchronouslyRunOperation:op];
    XCTAssertEqualObjects(expectedOutputString, op.outputString);
}

- (void)testBase64EncodeEmpty {
    NSData *            inputData;
    QCCBase64Encode *   op;
    NSString *          expectedOutputString;

    inputData = [NSData dataWithContentsOfURL:[[NSBundle bundleForClass:[self class]] URLForResource:@"plaintext-0" withExtension:@"dat"]];
    assert(inputData != nil);

    expectedOutputString = @"";
    assert(expectedOutputString != nil);

    op = [[QCCBase64Encode alloc] initWithInputData:inputData];
    op.addLineBreaks = YES;
    [[ToolCommon sharedInstance] synchronouslyRunOperation:op];
    XCTAssertEqualObjects(expectedOutputString, op.outputString);
}

- (void)testBase64Decode {
    NSString *          inputString;
    QCCBase64Decode *   op;
    NSData *            expectedOutputData;

    inputString = [NSString stringWithContentsOfURL:[[NSBundle bundleForClass:[self class]] URLForResource:@"test" withExtension:@"pem"] encoding:NSUTF8StringEncoding error:NULL];
    assert(inputString != nil);

    expectedOutputData = [NSData dataWithContentsOfURL:[[NSBundle bundleForClass:[self class]] URLForResource:@"test" withExtension:@"cer"]];
    assert(expectedOutputData != nil);

    op = [[QCCBase64Decode alloc] initWithInputString:inputString];
    [[ToolCommon sharedInstance] synchronouslyRunOperation:op];
    XCTAssertEqualObjects(expectedOutputData, op.outputData);
}

- (void)testBase64Throws {
    #pragma clang diagnostic push
    #pragma clang diagnostic ignored "-Wnonnull"
    XCTAssertThrows((void) [[QCCBase64Encode alloc] initWithInputData:nil]);
    XCTAssertThrows((void) [[QCCBase64Decode alloc] initWithInputString:nil]);
    #pragma clang diagnostic pop
}

@end
```

[Next](UnitTest-CryptorOperationsTests.m.md)[Previous](UnitTest-KeyDerivationOperationsTests.m.md)

