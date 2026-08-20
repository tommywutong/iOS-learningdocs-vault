---
title: Identity Services Programming Guide
apple_id: TP40004490
resource_type: Guide
platform: macOS
topic: Networking, Internet, & Web
technology: Collaboration
published: '2012-02-16'
source_url: https://developer.apple.com/library/archive/documentation/Networking/Conceptual/IdentityServices_ProgGuide/WorkingwithAccessControlLists/WorkingwithAccessControlLists.html
archived_at: '2026-07-15T08:18:13.049620Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Identity Services Programming Guide](Introduction%20to%20Identity%20Services%20Programming%20Guide.md)


[Next](Document%20Revision%20History.md)[Previous](Finding%20and%20Monitoring%20Identities.md)

# Working with Access Control Lists

A number of applications that take advantage of identities use them to control access to a file or service. The identities and their access levels are often stored in an access control list (ACL). The following chapter explains how to create an ACL, store it, and load it for use later.

An ACL can be maintained in any data object you want. This data object should be tailored based on your application’s needs. For example, if your application needs to store a list of only those users and groups who can access your service, then a simple array or set may suffice. However, if your application needs to store a list of identities and their access level, you might want to use a dictionary. [Listing 4-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2diojqfvbuqnznknlte) shows how to create a dictionary object for you ACL and then run the identity picker. The identities returned from the picker are stored in the dictionary object as a key-value pair, where the key is the identity and the value is the permissions.

__Listing 4-1__  Creating an ACL with the Collaboration framework

```
// Create a dictionary to use as your ACL
NSMutableDictionary *accessControlList = [[NSMutableDictionary alloc] init];

// Run the identity picker
if ([picker runModal] == NSOKButton) {
    NSArray *identities = [picker identities];
    NSEnumerator *enumerator = [identities objectEnumerator];


    // Enumerate over the returned identities,
    // and add each one to the ACL
    while ((nextIdentity = [enumerator nextObject])) {

        // Make sure to use the identity object as the key, and the permissions level as the value
        [accessControlList setObject:@"read-only" forKey:nextIdentity];
    }
}
```

If you are using the Core Services Identity API, you can create a similar ACL with a `CFDictionary` object, using `CSIdentity` objects as the keys.

When your application quits, it needs to store the ACL as a file. If your ACL is stored as an `NSDictionary` object, simply use the method `writeToFile:atomically:` to write the ACL to a plist file. When the file is written, each identity is stored as a persistent reference. The persistent reference of an identity is an opaque data object that is a faster, more reliable way to retrieve the identity from an identity authority than a UUID.

If you are not using a dictionary to house your ACL, use a persistent reference when you write the ACL to a file. In the Collaboration framework, use the method `persistentReference` to create a persistent reference for an identity or use the `NSCoding` protocol methods. In the Core Services Identity API, use the `CSIdentityCreatePersistentReference` method.

After you write your ACL to a file, your application needs to restore the ACL to a form it can access quickly. If you are using an `NSDictionary` object, instantiate a new object with the `dictionaryWithContentsOfFile:` method. Similarly, if you used the `NSCoding` protocol methods to archive the ACL, use the appropriate methods to unarchive the ACL. Either approach will also convert the persistent reference to an identity object automatically, so you can begin using the new dictionary object immediately. If an identity in the ACL has been removed, no conversion will take place.

If you wrote the ACL to a custom file format, you need to load the file back into memory, and load each persistent reference. You can instantiate the identity object from the persistent reference with the `identityWithPersistentReference:` method.

Retrieving an identity object in the Core Services API is a bit more involved. Once you have the presistent reference, create an identity query object using the `CSIdentityQueryCreateForPersistentReference` method. Then execute the query, and retrieve the returned identity objects. (For more information about querying an identity authority, see [Finding and Monitoring Identities](Finding%20and%20Monitoring%20Identities.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2diojqfvbuqnrnknltc)).

[Next](Document%20Revision%20History.md)[Previous](Finding%20and%20Monitoring%20Identities.md)

