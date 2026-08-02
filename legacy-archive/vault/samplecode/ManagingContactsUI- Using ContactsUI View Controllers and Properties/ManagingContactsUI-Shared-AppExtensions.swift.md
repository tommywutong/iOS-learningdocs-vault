---
title: 'ManagingContactsUI: Using ContactsUI View Controllers and Properties'
apple_id: TP40017633
resource_type: Sample Code
platform: iOS
topic: null
technology: ContactsUI
published: '2017-07-20'
source_url: https://developer.apple.com/library/archive/samplecode/ManagingContactsUI/Listings/ManagingContactsUI_Shared_AppExtensions_swift.html
archived_at: '2026-07-18T03:14:30.374229Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ManagingContactsUI: Using ContactsUI View Controllers and Properties](ManagingContactsUI-%20Using%20ContactsUI%20View%20Controllers%20and%20Properties.md)


[Next](ManagingContactsUI-Shared-Helper.swift.md)[Previous](ManagingContactsUI-Shared-LabelValue.swift.md)

# ManagingContactsUI/Shared/AppExtensions.swift

```swift
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Creates extensions for the CNContact, CNContactProperty, CNPostalAddress, and
  String classes.
*/

import UIKit
import Contacts

// MARK: - CNContact

extension CNContact {

    /**
        - returns: The formatted name of a contact if there is one and
                   "No Name", otherwise.
    */
    var formattedName: String {
        if let name = CNContactFormatter.string(from: self, style: .fullName) {
            return name.trim()
        }
        return AppConfiguration.TableViewCellLabels.namelessContact
    }
}

// MARK: - CNContactProperty

extension CNContactProperty {

    /// -returns: The name matching the key of the property.
    var nameMatchingKey: String? {
        switch self.key {
            case "emailAddresses": return "Email address"
            case "phoneNumbers": return "Phone numbers"
            case "postalAddresses": return "Postal address"
            default: break
        }
        return nil
    }

    /// -returns: The name matching the value of the property.
    var nameMatchingValue: String? {

        switch self.key {
            case "emailAddresses": return self.value as? String
            case "phoneNumbers":
                if let phoneNumber = self.value as? CNPhoneNumber {
                    return phoneNumber.stringValue
                }
            case "postalAddresses":
                if let address = self.value as? CNPostalAddress {
                    return address.formattedPostalAddress
                }
            default: break
        }
        return nil
    }

    /// -returns: The name matching the localized label of the property.
    var nameMatchingLocalizedLabel: String? {
        if let label = self.label {
            switch key {
                case "emailAddresses": return CNLabeledValue<NSString>.localizedString(forLabel: label)
                case "phoneNumbers": return CNLabeledValue<CNPhoneNumber>.localizedString(forLabel: label)
                case "postalAddresses": return CNLabeledValue<CNPostalAddress>.localizedString(forLabel: label)
                default: break
            }
        }
        return nil
    }
}

// MARK: - CNPostalAddress

extension CNPostalAddress {

    /// -returns: The formatted postal address.
    var formattedPostalAddress: String? {
        let adddress = [self.street, self.city, self.state, self.postalCode, self.country]
        let filteredArray = adddress.filter({ (item: String) in !item.isEmpty })

        if !filteredArray.isEmpty {
            return filteredArray.joined(separator: ", ")
        }
        return nil
    }
}

// MARK: - String

extension String {

    /// -returns: A string without white spaces and new lines.
    func trim() -> String {
        return self.trimmingCharacters(in: .whitespacesAndNewlines)
    }
}
```

[Next](ManagingContactsUI-Shared-Helper.swift.md)[Previous](ManagingContactsUI-Shared-LabelValue.swift.md)

