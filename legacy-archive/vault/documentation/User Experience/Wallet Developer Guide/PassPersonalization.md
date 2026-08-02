---
title: Wallet Developer Guide
apple_id: TP40012195
resource_type: Guide
platform: watchOS|iOS
topic: User Experience
technology: PassKit
published: '2018-01-16'
source_url: https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/PassKit_PG/PassPersonalization.html
archived_at: '2026-07-18T02:12:15.495564Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Wallet Developer Guide](index.md)



## Rewards Enrollment

Rewards enrollment lets you create a pass that prompts the user to sign up for a rewards program. These passes are referred to as personalizable passes, because the user provides personal information during signup that is used to update the pass.

> [!IMPORTANT]
> 

Personalizable passes can be distributed like any other pass. When the user installs a personalizable pass, it automatically triggers the following signup procedure:

1. Wallet presents a signup form that describes the program, requests the user’s personal information, and presents the program’s terms and conditions.
2. After the user completes the signup form, Wallet posts the user’s data and a personalization token to your server.
3. Your server creates an account for the user.
4. Your server signs the personalization token using the pass certificate, and returns the signed token.
5. Wallet verifies the signed token. If the verification fails, Wallet sends a warning to your logging endpoint.
6. Wallet makes a get request for the personalized pass.
7. Your server creates and returns a personalized pass.
8. Wallet removes the original, personalizable pass and installs the new personalized pass.

> [!NOTE]
> 

### Setting Up Pass Personalization

To support pass personalization, perform the following steps:

1. Create and distribute a personalizable pass.
2. Implement the web service’s `personalize` endpoint.
3. Implement the web service’s endpoint that returns personalized passes.

### Creating a Personalizable Pass

A personalizable pass is just a standard pass package with the following additional files:

- A `personalization.json` file.

  This file specifies the personal information requested by the signup form. It also contains a description of the program and (optionally) the program’s terms and conditions.
- A `personalizationLogo@XX.png` file.

  Use a 150 x 40 point png file. This logo is displayed at the top of the signup form.

The `personalization.json` file has the following top-level keys.

| Key name | Type | Description |
| --- | --- | --- |
| `requiredPersonalizationFields` | array | _Required._ The contents of this array define the data requested from the user. The signup form’s fields are generated based on these keys. |
| `description` | localizable string | _Required._ A brief description of the program. This is displayed on the signup sheet, under the personalization logo. |
| `termsAndConditions` | string | _Optional._ A description of the program’s terms and conditions. This string can contain HTML link tags to external content.  If present, this information is displayed after the user enters their personal information and taps the Next button. The user then has the option to agree to the terms, or to cancel out of the signup process. |

The `requiredPersonalizationFields` array contains one or more of the following keys.

| Key name | Description |
| --- | --- |
| `PKPassPersonalizationFieldName` | Prompts the user for their name. `fullName`, `givenName`, and `familyName` are submitted in the personalize request. |
| `PKPassPersonalizationFieldPostalCode` | Prompts the user for their postal code. `postalCode` and `ISOCountryCode` are submitted in the personalize request. |
| `PKPassPersonalizationFieldEmailAddress` | Prompts the user for their email address. `emailAddress` is submitted in the personalize request. |
| `PKPassPersonalizationFieldPhoneNumber` | Prompts the user for their phone number. `phoneNumber` is submitted in the personalize request. |

A example of the `personalization.json` content is shown below:

1. `{`
2. `"requiredPersonalizationFields" : [`
3. `"PKPassPersonalizationFieldName",`
4. `"PKPassPersonalizationFieldPostalCode",`
5. `"PKPassPersonalizationFieldEmailAddress",`
6. `"PKPassPersonalizationFieldPhoneNumber"`
7. `],`
8. `"description": "Enter your information to sign up and earn points.",`
9. `"termsAndConditions" : “Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.\n\n<a href='http://apple.com'>Tap Here for more Info</a>\n\n "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium."`
10. `}`

### Implementing the Web Service

After the user completes the signup form, Wallet sends a POST request to your web service. Implement the following endpoint to handle these requests:

POST request to _webServiceURL_`/`_version_`/passes/`_passTypeIdentifier_`/`_serialNumber_`/personalize`

__Parameters__

|  |  |
| --- | --- |
| **_webServiceURL_** | : The URL to your web service, as specified in the pass. For more information, see [Web Service Keys](https://developer.apple.com/library/archive/documentation/UserExperience/Reference/PassKit_Bundle/Chapters/TopLevel.html#//apple_ref/doc/uid/TP40012026-CH2-SW3). |
| **_version_** | : The protocol version—currently, v1. |
| **_passTypeIdentifier_** | : The pass’s type, as specified in the pass. For more information, see [Standard Keys](https://developer.apple.com/library/archive/documentation/UserExperience/Reference/PassKit_Bundle/Chapters/TopLevel.html#//apple_ref/doc/uid/TP40012026-CH2-SW2). |
| **_serialNumber_** | : The pass’s serial number, as specified in the pass. For more information, see [Standard Keys](https://developer.apple.com/library/archive/documentation/UserExperience/Reference/PassKit_Bundle/Chapters/TopLevel.html#//apple_ref/doc/uid/TP40012026-CH2-SW2). |

__Payload__

The POST payload is a JSON dictionary containing the following top level keys.

| Key name | Type | Description |
| --- | --- | --- |
| `personalizationToken` | string | _Required._ The personalization token for this request. Your server must sign and return this token. |
| `requiredPersonalizationInfo` | dictionary | _Required._ A dictionary containing the requested personal information. |

The `requiredPersonalizationInfo` dictionary contains one or more of the following keys.

| Key name | Type | Description |
| --- | --- | --- |
| `fullName` | string | _Optional._ The user’s full name, as entered by the user. |
| `givenName` | dictionary | _Optional._ The user’s given name, parsed from the full name.  This is the name bestowed upon an individual to differentiate them from other members of a group that share a family name (for example, “John”). In some locales, this is also known as a first name or forename. |
| `familyName` | dictionary | _Optional._ The user’s family name, parsed from the full name.  This is the name bestowed upon an individual to denote membership in a group or family (for example, “Appleseed”). |
| `emailAddress` | dictionary | _Optional._ The email address, as entered by the user. |
| `postalCode` | dictionary | _Optional._ The postal code, as entered by the user. |
| `ISOCountryCode` | dictionary | _Optional._ The user’s ISO country code. This key is only included when the system can deduce the country code. |
| `phoneNumber` | dictionary | _Optional._ The phone number, as entered by the user. |

A sample payload is shown below:

1. `{`
2. `“personalizationToken” : “324389RFHF32JOID2902F3JF23092FEJI02”,`
3. `“requiredPersonalizationInfo” : {`
4. `“fullName” : “John Appleseed”,`
5. `“givenName” : “John”,`
6. `“familyName” : “Appleseed”,`
7. `“emailAddress” : "john.appleseed@icloud.com",`
8. `“postalCode” : “95014”,`
9. `“ISOCountryCode” : “US”`
10. `}`
11. `}`

__Response__

Use the pass’s `passTypeIdentifier` and `serialNumber` to uniquely identify this user. After the user’s personal information is uploaded to your system, save this information so that you can later retrieve it using the `passTypeIdentifier` and `serialNumber`.

Next, sign and return the personalization token using the pass certificate. Return this signature in the payload of the response, using an `application/octet-stream` content type.

### Implementing the Personalized Pass Web Service

After verifying the personalization token’s signature, Wallet attempts to download the personalized pass by sending a GET request to your web service. Implement the following endpoint to handle these requests.

GET request to _webServiceURL_`/`_version_`/passes/`_passTypeIdentifier_`/`_serialNumber_

__Parameters__

|  |  |
| --- | --- |
| **_webServiceURL_** | : The URL to your web service, as specified in the pass. For more information, see [Web Service Keys](https://developer.apple.com/library/archive/documentation/UserExperience/Reference/PassKit_Bundle/Chapters/TopLevel.html#//apple_ref/doc/uid/TP40012026-CH2-SW3). |
| **_version_** | : The protocol version—currently, v1. |
| **_passTypeIdentifier_** | : The pass’s type, as specified in the pass. For more information, see [Standard Keys](https://developer.apple.com/library/archive/documentation/UserExperience/Reference/PassKit_Bundle/Chapters/TopLevel.html#//apple_ref/doc/uid/TP40012026-CH2-SW2). |
| **_serialNumber_** | : The pass’s serial number, as specified in the pass. For more information, see [Standard Keys](https://developer.apple.com/library/archive/documentation/UserExperience/Reference/PassKit_Bundle/Chapters/TopLevel.html#//apple_ref/doc/uid/TP40012026-CH2-SW2). |

__Response__

The server looks up the user’s account information using the `passTypeIdentifier` and `serialNumber`. It then creates and returns a personalized pass for the user. This pass must not contain the `personalization.json` file.

Because this pass is signed by your server, Wallet automatically validates the pass and installs it, replacing the original, personalizable pass.

[Interacting with Passes in Your App](Apps.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdcojvfvbuqnrnknltc)
