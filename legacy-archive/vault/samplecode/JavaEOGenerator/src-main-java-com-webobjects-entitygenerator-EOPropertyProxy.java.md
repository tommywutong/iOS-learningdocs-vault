---
title: JavaEOGenerator
apple_id: DTS10004471
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2007-11-14'
source_url: https://developer.apple.com/library/archive/samplecode/JavaEOGenerator/Listings/src_main_java_com_webobjects_entitygenerator_EOPropertyProxy_java.html
archived_at: '2026-07-18T03:13:15.036969Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [JavaEOGenerator](JavaEOGenerator.md)


[Next](src-main-java-com-webobjects-entitygenerator-EORelationshipProxy.java.md)[Previous](src-main-java-com-webobjects-entitygenerator-EOFetchSpecificationProxy.java.md)

# src/main/java/com/webobjects/entitygenerator/EOPropertyProxy.java

```
/*
 * Copyright 2005 - 2007  Apple, Inc. All rights reserved.
 *
 * IMPORTANT:  This Apple software is supplied to you by Apple, Inc. (ÒAppleÓ) in consideration of your agreement to the following terms, and your use, installation, modification or redistribution of this Apple software constitutes acceptance of these terms.  If you do not agree with these terms, please do not use, install, modify or redistribute this Apple software.
 *
 * In consideration of your agreement to abide by the following terms, and subject to these terms, Apple grants you a personal, non-exclusive license, under AppleÕs copyrights in this original Apple software (the ÒApple SoftwareÓ), to use, reproduce, modify and redistribute the Apple Software, with or without modifications, in source and/or binary forms; provided that if you redistribute the Apple Software in its entirety and without modifications, you must retain this notice and the following text and disclaimers in all such redistributions of the Apple Software.  Neither the name, trademarks, service marks or logos of Apple Computer, Inc. may be used to endorse or promote products derived from the Apple Software without specific prior written permission from Apple.  Except as expressly stated in this notice, no other rights or licenses, express or implied, are granted by Apple herein, including but not limited to any patent rights that may be infringed by your derivative works or by other works in which the Apple Software may be incorporated.
 *
 * The Apple Software is provided by Apple on an "AS IS" basis.  APPLE MAKES NO WARRANTIES, EXPRESS OR IMPLIED, INCLUDING WITHOUT LIMITATION THE IMPLIED WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE, REGARDING THE APPLE SOFTWARE OR ITS USE AND OPERATION ALONE OR IN COMBINATION WITH YOUR PRODUCTS.
 *
 * IN NO EVENT SHALL APPLE BE LIABLE FOR ANY SPECIAL, INDIRECT, INCIDENTAL OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) ARISING IN ANY WAY OUT OF THE USE, REPRODUCTION, MODIFICATION AND/OR DISTRIBUTION OF THE APPLE SOFTWARE, HOWEVER CAUSED AND WHETHER UNDER THEORY OF CONTRACT, TORT (INCLUDING NEGLIGENCE), STRICT LIABILITY OR OTHERWISE, EVEN IF APPLE HAS BEEN  ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 *
 */
package com.webobjects.entitygenerator;

import com.webobjects.eoaccess.EOProperty;
import com.webobjects.generator.GeneratorProxy;

/**
 * This class is a proxy to enable code generation for bindings of named fetch specification in the model
 *
 * @param <T>
 *            Type of property (attribute or relationship)
 */
public abstract class EOPropertyProxy<T extends EOProperty> extends GeneratorProxy<T> {

    /**
     * Constructor
     *
     * @param property
     */
    public EOPropertyProxy(T property) {
        super(property.name(), property);
    }

    /**
     * Constructor
     *
     * @param name
     * @param property
     */
    public EOPropertyProxy(String name, T property) {
        super(name, property);
    }

    /**
     * Return the binding class name
     *
     * @return binding class name
     */
    public abstract String className();

    /**
     * Return the binding value type class name
     *
     * @return binding value type class name
     */
    public abstract String valueTypeClassName();
}
```

[Next](src-main-java-com-webobjects-entitygenerator-EORelationshipProxy.java.md)[Previous](src-main-java-com-webobjects-entitygenerator-EOFetchSpecificationProxy.java.md)

