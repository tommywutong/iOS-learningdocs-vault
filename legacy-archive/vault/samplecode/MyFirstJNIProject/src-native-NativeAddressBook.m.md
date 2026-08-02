---
title: MyFirstJNIProject
apple_id: DTS10003687
resource_type: Sample Code
platform: Java|macOS
topic: Cross Platform
technology: null
published: '2011-03-01'
source_url: https://developer.apple.com/library/archive/samplecode/MyFirstJNIProject/Listings/src_native_NativeAddressBook_m.html
archived_at: '2026-07-18T03:16:36.211609Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MyFirstJNIProject](MyFirstJNIProject.md)


[Next](Document%20Revision%20History.md)[Previous](src-java-com-example-JNIAddressBook.java.md)

# src/native/NativeAddressBook.m

```objc
/*
     File: NativeAddressBook.m
 Abstract: Implements basic Java/Foundation object graph conversion with AddressBook data types.
  Version: 2.1

 Disclaimer: IMPORTANT:  This Apple software is supplied to you by Apple
 Inc. ("Apple") in consideration of your agreement to the following
 terms, and your use, installation, modification or redistribution of
 this Apple software constitutes acceptance of these terms.  If you do
 not agree with these terms, please do not use, install, modify or
 redistribute this Apple software.

 In consideration of your agreement to abide by the following terms, and
 subject to these terms, Apple grants you a personal, non-exclusive
 license, under Apple's copyrights in this original Apple software (the
 "Apple Software"), to use, reproduce, modify and redistribute the Apple
 Software, with or without modifications, in source and/or binary forms;
 provided that if you redistribute the Apple Software in its entirety and
 without modifications, you must retain this notice and the following
 text and disclaimers in all such redistributions of the Apple Software.
 Neither the name, trademarks, service marks or logos of Apple Inc. may
 be used to endorse or promote products derived from the Apple Software
 without specific prior written permission from Apple.  Except as
 expressly stated in this notice, no other rights or licenses, express or
 implied, are granted by Apple herein, including but not limited to any
 patent rights that may be infringed by your derivative works or by other
 works in which the Apple Software may be incorporated.

 The Apple Software is provided by Apple on an "AS IS" basis.  APPLE
 MAKES NO WARRANTIES, EXPRESS OR IMPLIED, INCLUDING WITHOUT LIMITATION
 THE IMPLIED WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY AND FITNESS
 FOR A PARTICULAR PURPOSE, REGARDING THE APPLE SOFTWARE OR ITS USE AND
 OPERATION ALONE OR IN COMBINATION WITH YOUR PRODUCTS.

 IN NO EVENT SHALL APPLE BE LIABLE FOR ANY SPECIAL, INDIRECT, INCIDENTAL
 OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
 SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
 INTERRUPTION) ARISING IN ANY WAY OUT OF THE USE, REPRODUCTION,
 MODIFICATION AND/OR DISTRIBUTION OF THE APPLE SOFTWARE, HOWEVER CAUSED
 AND WHETHER UNDER THEORY OF CONTRACT, TORT (INCLUDING NEGLIGENCE),
 STRICT LIABILITY OR OTHERWISE, EVEN IF APPLE HAS BEEN ADVISED OF THE
 POSSIBILITY OF SUCH DAMAGE.

 Copyright (C) 2011 Apple Inc. All Rights Reserved.

 */

#import <AddressBook/AddressBook.h>
#import <JavaNativeFoundation/JavaNativeFoundation.h> // helper framework for Cocoa and JNI development

#import "com_example_app_addressbook_NativeAddressBook.h" // generated from NativeAddressBook.java


/* 
 * Entry point from Java though JNI to call into the Mac OS X Address Book framework,
 * and create Java objects from the Objective-C Foundation objects returned from the
 * Address Book.
 * 
 * Uses JavaNativeFoundation, a sub-framework of the JavaVM.framework to setup autorelease
 * pools, catch NSExceptions, and re-throw them as Java exceptions. JNF provides a layer
 * on top of conventional C-based JNI to ease interoperability with Cocoa.
 *
 * For more information on conventional JNI on Mac OS X, see:
 * <http://developer.apple.com/technotes/tn2005/tn2147.html>
 * 
 * For more information on JavaNativeFoundation, see:
 * <http://developer.apple.com/library/mac/#documentation/CrossPlatform/Reference/JavaNativeFoundation_Functions>
 */


// coerces an ABPerson into a map
@interface ABPersonCoercer : NSObject<JNFTypeCoercion> { }
+ (ABPersonCoercer *) personCoercer;
@end

// coerces an ABMultiValue into a list of single key/value maps
@interface ABMultiValueCoercer : NSObject<JNFTypeCoercion> { }
+ (ABMultiValueCoercer *) multiValueCoercer;
@end


/*
 * Class:     com_example_app_addressbook_NativeAddressBook
 * Method:    nativeGetMyUID
 * Signature: ()Ljava/lang/String;
 */
JNIEXPORT jstring JNICALL Java_com_example_app_addressbook_NativeAddressBook_nativeGetMyUID
(JNIEnv *env, jclass clazz)
{
    jstring myUID = NULL; // need to declare outside of the JNF_COCOA_ENTER/EXIT @try/catch scope

JNF_COCOA_ENTER(env);

    NSString *myIdAsStr = nil;
    NSString **myIdAsStrPtr = &myIdAsStr; // work around immutability of myIdAsStr inside block
    [JNFRunLoop performOnMainThreadWaiting:YES withBlock:^() {
        ABPerson *me = [[ABAddressBook sharedAddressBook] me];
        (*myIdAsStrPtr) = [[me uniqueId] retain];
    }];

    // convert the NSString to a Java string while on Java's thread
    myUID = JNFNSToJavaString(env, myIdAsStr);
    [myIdAsStr release];

JNF_COCOA_EXIT(env);

    return myUID;
}


/*
 * Class:     com_example_app_addressbook_NativeAddressBook
 * Method:    nativeGetAddressBookContacts
 * Signature: ()Ljava/util/List;
 */
JNIEXPORT jobject JNICALL Java_com_example_app_addressbook_NativeAddressBook_nativeGetAddressBookContacts
(JNIEnv *env, jclass clazz)
{
    jobject persons = NULL; // need to declare outside of the JNF_COCOA_ENTER/EXIT @try/catch scope

JNF_COCOA_ENTER(env);

    // get all people into an array on the main thread
    NSMutableArray *people = [NSMutableArray array];
    [JNFRunLoop performOnMainThreadWaiting:YES withBlock:^() {
        ABAddressBook *addressBook = [ABAddressBook sharedAddressBook];
        [people addObjectsFromArray:[addressBook people]];
    }];

    // create and load a coercer with additional coercions to convert each type of object
    JNFTypeCoercer *coercer = [JNFDefaultCoercions defaultCoercer];
    [coercer addCoercion:[ABPersonCoercer personCoercer] forNSClass:[ABPerson class] javaClass:nil];
    [coercer addCoercion:[ABMultiValueCoercer multiValueCoercer] forNSClass:[ABMultiValue class] javaClass:nil];

    // recursively decend into the object graph of "people", and 
    // convert every NSObject into a corresponding Java object
    persons = [coercer coerceNSObject:people withEnv:env];

JNF_COCOA_EXIT(env);

    return persons;
}

/*
 * Class:     com_example_app_addressbook_NativeAddressBook
 * Method:    nativeEditContact
 * Signature: (Ljava/lang/String;)V
 */
JNIEXPORT void JNICALL Java_com_example_app_addressbook_NativeAddressBook_nativeEditContact
(JNIEnv *env, jclass clazz, jstring uid)
{
JNF_COCOA_ENTER(env);

    // convert the string while still on Java's thread
    NSString *urlString = [NSString stringWithFormat:@"addressbook://%@?edit", JNFJavaToNSString(env, uid)];

    // punt the work over to the AppKit thread, and don't bother to wait
    [JNFRunLoop performOnMainThreadWaiting:NO withBlock:^() {
        [[NSWorkspace sharedWorkspace] openURL:[NSURL URLWithString:urlString]];
    }];

JNF_COCOA_EXIT(env);
}


// puts all the properties of an ABPerson into an NSDictionary, and uses the same 
// root coercer to transform that NSDictionary into a java.util.Map
@implementation ABPersonCoercer

+ (ABPersonCoercer *) personCoercer {
    return [[[ABPersonCoercer alloc] init] autorelease];
}

- (jobject) coerceNSObject:(id)obj withEnv:(JNIEnv *)env usingCoercer:(JNFTypeCoercion *)coercer {
    ABPerson *person = obj;
    NSMutableDictionary *dict = [NSMutableDictionary dictionary];

    NSArray *props = [ABPerson properties];
    for (NSString *propName in props) {
        if (propName == nil) continue;

        id prop = [person valueForProperty:propName]; 
        if (prop == nil) continue;

        [dict setValue:prop forKey:propName];
    }

    return [coercer coerceNSObject:dict withEnv:env usingCoercer:coercer];
}

- (id) coerceJavaObject:(jobject)obj withEnv:(JNIEnv *)env usingCoercer:(JNFTypeCoercion *)coercer {
    return nil; // exercise left to the reader
}

@end


// creates an NSArray for each ABMultiValue, and puts each key/value pair into its own NSDictionary,
// then uses the same root coercer to transform them into java.util.Lists and java.util.Maps
@implementation ABMultiValueCoercer

+ (ABMultiValueCoercer *) multiValueCoercer {
    return [[[ABMultiValueCoercer alloc] init] autorelease];
}

- (jobject) coerceNSObject:(id)obj withEnv:(JNIEnv *)env usingCoercer:(JNFTypeCoercion *)coercer {
    ABMultiValue *multiValue = obj;

    NSUInteger count = [multiValue count];
    NSMutableArray *values = [NSMutableArray arrayWithCapacity:count];

    NSUInteger i;
    for (i = 0; i < count; i++) {
        NSString *label = [multiValue labelAtIndex:i];
        id object = [multiValue valueAtIndex:i];

        [values addObject:[NSDictionary dictionaryWithObjects:&object forKeys:&label count:1]];
    }

    return [coercer coerceNSObject:values withEnv:env usingCoercer:coercer];
}

- (id) coerceJavaObject:(jobject)obj withEnv:(JNIEnv *)env usingCoercer:(JNFTypeCoercion *)coercer {
    return nil; // exercise left to the reader
}

@end
```

[Next](Document%20Revision%20History.md)[Previous](src-java-com-example-JNIAddressBook.java.md)

