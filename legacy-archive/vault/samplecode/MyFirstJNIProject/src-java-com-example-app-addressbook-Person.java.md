---
title: MyFirstJNIProject
apple_id: DTS10003687
resource_type: Sample Code
platform: Java|macOS
topic: Cross Platform
technology: null
published: '2011-03-01'
source_url: https://developer.apple.com/library/archive/samplecode/MyFirstJNIProject/Listings/src_java_com_example_app_addressbook_Person_java.html
archived_at: '2026-07-18T03:16:35.987268Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MyFirstJNIProject](MyFirstJNIProject.md)


[Next](src-java-com-example-app-addressbook-PersonSelectionListener.java.md)[Previous](src-java-com-example-app-addressbook-NativeAddressBook.java.md)

# src/java/com/example/app/addressbook/Person.java

```
//     File: Person.java
// Abstract: A representation of an address book entry.
//  Version: 2.1
// 
// Disclaimer: IMPORTANT:  This Apple software is supplied to you by Apple
// Inc. ("Apple") in consideration of your agreement to the following
// terms, and your use, installation, modification or redistribution of
// this Apple software constitutes acceptance of these terms.  If you do
// not agree with these terms, please do not use, install, modify or
// redistribute this Apple software.
// 
// In consideration of your agreement to abide by the following terms, and
// subject to these terms, Apple grants you a personal, non-exclusive
// license, under Apple's copyrights in this original Apple software (the
// "Apple Software"), to use, reproduce, modify and redistribute the Apple
// Software, with or without modifications, in source and/or binary forms;
// provided that if you redistribute the Apple Software in its entirety and
// without modifications, you must retain this notice and the following
// text and disclaimers in all such redistributions of the Apple Software.
// Neither the name, trademarks, service marks or logos of Apple Inc. may
// be used to endorse or promote products derived from the Apple Software
// without specific prior written permission from Apple.  Except as
// expressly stated in this notice, no other rights or licenses, express or
// implied, are granted by Apple herein, including but not limited to any
// patent rights that may be infringed by your derivative works or by other
// works in which the Apple Software may be incorporated.
// 
// The Apple Software is provided by Apple on an "AS IS" basis.  APPLE
// MAKES NO WARRANTIES, EXPRESS OR IMPLIED, INCLUDING WITHOUT LIMITATION
// THE IMPLIED WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY AND FITNESS
// FOR A PARTICULAR PURPOSE, REGARDING THE APPLE SOFTWARE OR ITS USE AND
// OPERATION ALONE OR IN COMBINATION WITH YOUR PRODUCTS.
// 
// IN NO EVENT SHALL APPLE BE LIABLE FOR ANY SPECIAL, INDIRECT, INCIDENTAL
// OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
// SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
// INTERRUPTION) ARISING IN ANY WAY OUT OF THE USE, REPRODUCTION,
// MODIFICATION AND/OR DISTRIBUTION OF THE APPLE SOFTWARE, HOWEVER CAUSED
// AND WHETHER UNDER THEORY OF CONTRACT, TORT (INCLUDING NEGLIGENCE),
// STRICT LIABILITY OR OTHERWISE, EVEN IF APPLE HAS BEEN ADVISED OF THE
// POSSIBILITY OF SUCH DAMAGE.
// 
// Copyright (C) 2011 Apple Inc. All Rights Reserved.
// 

package com.example.app.addressbook;

import java.util.*;

/**
 * Data model class for everyone records vended from the Mac OS X address book.
 * 
 * Decodes the data structures returned from JNI, by simply selecting the
 * first string value it finds. More sophisticated models that return lists
 * of email, chat, and phone numbers are an exercise left to the reader.
 * 
 * This model stores its values in a HashMap cache instead of instance variables
 * for sake of clarity and terseness. It is not thread-safe, and is currently only
 * used from the Swing event dispatch thread (EDT).
 */
public class Person {
    static final String
        FIRST = "First", MIDDLE = "Middle", LAST = "Last",
        EMAIL = "Email", PHONE = "Phone", CHAT = "AIMInstant",
        UID = "UID", FULL_NAME = "@FullName@", SEARCH_TEXT = "@SearchText@";

    static final Comparator<Person> SORT_BY_FIRST = new FirstNameSorter();
    static final Comparator<Person> SORT_BY_LAST = new LastNameSorter();

    final Map<String, ?> rawAttributes;
    final Map<String, String> cache = new HashMap<String, String>();

    public Person(final Map<String, ?> rawAttributes) {
        this.rawAttributes = rawAttributes;
    }

    // direct objects from the addressbook
    public String getFirstName()    { return getCached(FIRST); }
    public String getMiddleName()   { return getCached(MIDDLE); }
    public String getLastName()     { return getCached(LAST); }
    public String getEmail()        { return getCached(EMAIL); }
    public String getPhone()        { return getCached(PHONE); }
    public String getChat()         { return getCached(CHAT); }
    public String getUID()          { return getCached(UID); }

    private String getCached(final String key) {
        final String cachedValue = cache.get(key);
        if (cachedValue != null) return cachedValue;

        final String value = getFirstStringOf(rawAttributes.get(key));
        cache.put(key, value);
        return value;
    }

    // digs into collections and pulls out the first String it finds
    private static String getFirstStringOf(final Object object) {
        if (object instanceof String) return (String)object;
        if (object instanceof List<?>) {
            return getFirstStringOf(((List<?>)object).get(0));
        }
        if (object instanceof Map<?,?>) {
            return getFirstStringOf(((Map<?,?>)object).values().iterator().next());
        }
        return "";
    }

    // synthesized property
    public String getFullName() {
        final String name = cache.get(FULL_NAME);
        if (name != null) return name;

        final StringBuilder fullName = new StringBuilder();
        append(fullName, getFirstName(), false);
        append(fullName, getMiddleName(), true);
        append(fullName, getLastName(), true);

        final String newName = fullName.toString();
        cache.put(FULL_NAME, newName);
        return newName;
    }

    // synthesized property, returns lowercase text
    public String getFullSearchText() {
        final String fullSearchText = cache.get(SEARCH_TEXT);
        if (fullSearchText != null) return fullSearchText;

        final StringBuilder fullText = new StringBuilder(getFullName());
        append(fullText, getEmail(), true);
        append(fullText, getChat(), true);

        final String text = fullText.toString().toLowerCase();
        cache.put(SEARCH_TEXT, text);
        return text;
    }

    // string building helper
    private static void append(final StringBuilder builder, final String value, final boolean space) {
        if (value == null || "".equals(value)) return;
        if (space) builder.append(' ');
        builder.append(value);
    }

    static class FirstNameSorter implements Comparator<Person> {
        public int compare(final Person o1, final Person o2) {
            return o1.getFirstName().compareTo(o2.getFirstName());
        }
    }

    static class LastNameSorter implements Comparator<Person> {
        public int compare(final Person o1, final Person o2) {
            return o1.getLastName().compareTo(o2.getLastName());
        }
    }
}
```

[Next](src-java-com-example-app-addressbook-PersonSelectionListener.java.md)[Previous](src-java-com-example-app-addressbook-NativeAddressBook.java.md)

