---
title: Over-the-Air Profile Delivery and Configuration
apple_id: TP40009505
resource_type: Guide
platform: iOS
topic: null
technology: null
published: '2018-04-09'
source_url: https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/iPhoneOTAConfiguration/ConfigurationProfileExamples/ConfigurationProfileExamples.html
archived_at: '2026-07-18T01:33:03.593017Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Over-the-Air Profile Delivery and Configuration](Introduction.md)


[Next](Document%20Revision%20History.md)[Previous](Creating%20a%20Profile%20Server%20for%20Over-The-Air%20Enrollment%20and%20Configuration.md)

# Configuration Profile Examples

This appendix includes two sections. The first, [Configuration Profile Payload Code Example](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tkmbvfvbuqnbnknlte), shows how to construct a basic profile payload programmatically. The second, [Sample Responses](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tkmbvfvbuqnbnknltg), shows examples of property lists that might be exchanged during a typical SCEP enrollment session.

This example of a configuration profile payload shown in Listing A-1 contains a webclip that points the user to an intranet site and provides a payload to allow the phone to enroll an SSL client authentication cert that will be required to access the protected assets.

__Listing A-1__  `client_cert_configuration_payload` function

```
def client_cert_configuration_payload(request)

    webclip_payload = general_payload()

    webclip_payload['PayloadIdentifier'] = "com.acme.webclip.intranet"
    webclip_payload['PayloadType'] = "com.apple.webClip.managed" # do not modify

    # strings that show up in UI, customisable
    webclip_payload['PayloadDisplayName'] = "ACME Inc."
    webclip_payload['PayloadDescription'] = "Creates a link to the ACME intranet on the home screen"

    # allow user to remove webclip
    webclip_payload['IsRemovable'] = true

    # the link
    webclip_payload['Label'] = "ACME Inc."
    webclip_payload['URL'] = "https://" + service_address(request).split(":")[0] # + ":4443/"
```

The webclip creates an icon that will take the user to the URL mentioned. In this case we allow the user to delete the webclip.

```
    client_cert_payload = scep_cert_payload(request, "Client Authentication", "foo");
```

The client certificate is enrolled by creating an SCEP payload similar to the one used for decrypting an encrypted payload. In a real-world implementation, you typically add additional parameters to specify key usage, policies, and subject alternative names to make it easier for the server to match the enrolled identity with a particular user and that user’s capabilities.

```
    Plist::Emit.dump([webclip_payload, client_cert_payload])

end
```

This function ends by dumping the raw array of payloads. The caller wraps them in a configuration profile and signs them, as shown in [Listing 2-8](Creating%20a%20Profile%20Server%20for%20Over-The-Air%20Enrollment%20and%20Configuration.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tkmbvfvbuqmrnknltcoi).

For more information about the types of payloads that are available, see the [Configuration Profile Reference](https://developer.apple.com/library/archive/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1).

This section includes sample profiles that illustrate over-the-air enrollment and configuration phases. These are excerpts and your requirements will vary from the examples. For syntax assistance, see the details provided earlier in this appendix. For a description of each phase, see [Over-the-Air Profile Delivery Concepts](Over-the-Air%20Profile%20Delivery%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tkmbvfvbuqmznknltc).


```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple Inc//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
    <dict>
        <key>PayloadContent</key>
        <dict>
            <key>URL</key>
            <string>https://profileserver.example.com/iphone</string>
            <key>DeviceAttributes</key>
            <array>
                <string>UDID</string>
                <string>IMEI</string>
                <string>ICCID</string>
                <string>VERSION</string>
                <string>PRODUCT</string>
            </array>
            <key>Challenge</key>

            <string>optional challenge</string>

or

            <data>base64-encoded</data>

        </dict>
        <key>PayloadOrganization</key>
        <string>Example Inc.</string>
        <key>PayloadDisplayName</key>
        <string>Profile Service</string>
        <key>PayloadVersion</key>
        <integer>1</integer>
        <key>PayloadUUID</key>
        <string>fdb376e5-b5bb-4d8c-829e-e90865f990c9</string>
        <key>PayloadIdentifier</key>
        <string>com.example.mobileconfig.profile-service</string>
        <key>PayloadDescription</key>
        <string>Enter device into the Example Inc encrypted profile service</string>
        <key>PayloadType</key>
        <string>Profile Service</string>
    </dict>
</plist>
```



```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
    <dict>
        <key>UDID</key>
        <string></string>
        <key>VERSION</key>
        <string>7A182</string>
        <key>MAC_ADDRESS_EN0</key>
        <string>00:00:00:00:00:00</string>
        <key>CHALLENGE</key>

either:

        <string>String</string>

or:

        <data>"base64 encoded data"</data>

    </dict>
</plist>
```



```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple Inc//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
    <dict>
        <key>PayloadVersion</key>
        <integer>1</integer>
        <key>PayloadUUID</key>
        <string>Ignored</string>
        <key>PayloadType</key>
        <string>Configuration</string>
        <key>PayloadIdentifier</key>
        <string>Ignored</string>
        <key>PayloadContent</key>
        <array>
            <dict>
                <key>PayloadContent</key>
                <dict>
                    <key>URL</key>
                    <string>https://scep.example.com/scep</string>
                    <key>Name</key>
                    <string>EnrollmentCAInstance</string>
                    <key>Subject</key>
                    <array>
                        <array>
                            <array>
                                <string>O</string>
                                <string>Example, Inc.</string>
                            </array>
                        </array>
                        <array>
                            <array>
                                <string>CN</string>
                                <string>User Device Cert</string>
                            </array>
                        </array>
                    </array>
                    <key>Challenge</key>
                    <string>...</string>
                    <key>Keysize</key>
                    <integer>1024</integer>
                    <key>Key Type</key>
                    <string>RSA</string>
                    <key>Key Usage</key>
                    <integer>5</integer>
                </dict>
                <key>PayloadDescription</key>
                <string>Provides device encryption identity</string>
                <key>PayloadUUID</key>
                <string>fd8a6b9e-0fed-406f-9571-8ec98722b713</string>
                <key>PayloadType</key>
                <string>com.apple.security.scep</string>
                <key>PayloadDisplayName</key>
                <string>Encryption Identity</string>
                <key>PayloadVersion</key>
                <integer>1</integer>
                <key>PayloadOrganization</key>
                <string>Example, Inc.</string>
                <key>PayloadIdentifier</key>
                <string>com.example.profileservice.scep</string>
            </dict>
        </array>
    </dict>
</plist>
```



```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
    <dict>
        <key>UDID</key>
        <string></string>
        <key>VERSION</key>
        <string>7A182</string>
        <key>MAC_ADDRESS_EN0</key>
        <string>00:00:00:00:00:00</string>
    </dict>
</plist>
```

[Next](Document%20Revision%20History.md)[Previous](Creating%20a%20Profile%20Server%20for%20Over-The-Air%20Enrollment%20and%20Configuration.md)

