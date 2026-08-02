---
title: Over-the-Air Profile Delivery and Configuration
apple_id: TP40009505
resource_type: Guide
platform: iOS
topic: null
technology: null
published: '2018-04-09'
source_url: https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/iPhoneOTAConfiguration/OTASecurity/OTASecurity.html
archived_at: '2026-07-18T01:33:03.712396Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Over-the-Air Profile Delivery and Configuration](Introduction.md)


[Next](Creating%20a%20Profile%20Server%20for%20Over-The-Air%20Enrollment%20and%20Configuration.md)[Previous](Introduction.md)

# Over-the-Air Profile Delivery Concepts

The process of over-the-air enrollment and configuration is divided into three phases: authentication, enrollment, and device configuration. These phases are described in the sections that follow.

This process is illustrated in Directory Services.

__Figure 1-1__  Device registration process

!!

The authentication phase serves two purposes. First, it ensures that incoming enrollment requests are from authorized users. Second, it captures information about the user’s device for use in the certificate enrollment process.

When enrolling a device, the server can require authentication by the user, the device, or both.

User authentication can be enforced at the time the user goes to the enroll URL. To authenticate the user, you can use any web authentication scheme, whether part of HTTP (for example, basic auth or NTML) or a separate authentication scheme implemented by a CGI script. You can even use a hybrid scheme, such as combining digest authentication with a CGI-managed list of authorized users.

You can also check the device against a list of authorized devices if desired.

The steps in the authentication phase are:

1. The user visits the root URL (`/`) and gets a welcome message. This message is provided by the handler described in [Welcome Page (/) URL Handler](Creating%20a%20Profile%20Server%20for%20Over-The-Air%20Enrollment%20and%20Configuration.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tkmbvfvbuqmrnknltemy).
2. The user visits the certificate authority URL (`/CA`) to get the root cert (if needed). On the server, this URL is handled by code described in [Root Certificate (/CA) URL Handler](Creating%20a%20Profile%20Server%20for%20Over-The-Air%20Enrollment%20and%20Configuration.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tkmbvfvbuqmrnknltena).) This is only required for self-signed root CA certs.
3. The user visits the enrollment URL (`/enroll`) to start the enrollment process. In this step, the user is prompted to authenticate himself or herself using HTTP basic auth (in this example) or using existing directory services.
4. The server’s enrollment handler (described in [Enrollment (/enroll) URL Handler](Creating%20a%20Profile%20Server%20for%20Over-The-Air%20Enrollment%20and%20Configuration.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tkmbvfvbuqmrnknlteni)) determines whether the user is allowed to enroll a device. If the device is allowed to enroll, the server sends it a profile service payload ([Listing 2-5](Creating%20a%20Profile%20Server%20for%20Over-The-Air%20Enrollment%20and%20Configuration.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tkmbvfvbuqmrnknltcna)).

   This profile service payload (`.mobileconfig`) contains a request for additional device-specific information that the device must provide in the next step.

   The payload may, at your option, include a `Challenge` token so that the server can associate the request with the original user. This allows you to customize the configuration process for each user, if desired. This value should be something that can be verified, but is not easily guessable. For example, you could store a random value into a database and associate it with the user’s login credentials. The details of this functionality are site specific.

   The device attributes that the service can request are the iOS version, Wi-Fi device ID (MAC Address), product type (for example, iPhone 3GS returns `iPhone2,1`), phone equipment ID (IMEI), and SIM card identifier (ICCID).

   For a sample profile service payload, see [Sample Phase 1 Server Response](Configuration%20Profile%20Examples.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tkmbvfvbuqnbnknlti).

In the second phase, enrollment, a device contacts the certificate authority and obtains a signed X.509 identity certificate, which is then used for encryption.

To acquire an identity, a device first generates an asymmetric key pair and stores it in its keychain. The secrets in this keychain can be read only by that specific device.

The device then sends its public key to a certificate authority (CA), which sends back a signed X.509 certificate. This certificate, coupled with the private key on the device, form an identity.

To make this exchange possible, iOS supports the simple certificate enrollment protocol (SCEP). SCEP is a communication protocol that provides a networked front end to a private certificate authority. Support for SCEP is provided by a number of certificate authorities, and there are complete open-source software implementations of certificate authorities with SCEP support.

The front end service can be set up to gate access by means of a challenge, which in practice is an authorization token (a one-time password, or a signed/encrypted blob containing user/device info) to allow automatic issuing of a certificate.

The steps in the enrollment phase are:

1. The user accepts the installation of the profile received in phase 1.
2. The device looks up the requested attributes, adds the challenge response (if provided), signs the response using the device’s built-in identity (an Apple-issued certificate), and sends it back to the profile distribution service using HTTP POST.

   In the case of this example, the device sends this response to the `/profile` URL.

   For a sample profile from this phase, see [Sample Phase 2 Device Response](Configuration%20Profile%20Examples.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tkmbvfvbuqnbnknltk).
3. The server’s profile request handler (described in [Profile Request (/profile) URL Handler](Creating%20a%20Profile%20Server%20for%20Over-The-Air%20Enrollment%20and%20Configuration.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tkmbvfvbuqmrnknltenq)) sends back a configuration profile that instructs the device to enroll using SCEP as described in [Phase 2: Certificate Enrollment (X.509 Identities and SCEP)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tkmbvfvbuqmznknltk). The server should sign this profile.

   For a sample configuration profile, see [Sample Phase 3 Server Response With SCEP Specifications](Configuration%20Profile%20Examples.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tkmbvfvbuqnbnknltm).
4. The device enrolls using SCEP, resulting in a valid identity certificate installed on the device.

The third phase of over-the-air profile delivery and configuration is the actual profile delivery itself. In this phase, the server sends a profile that has been customized for a particular device.

In some environments, it is important to make sure that corporate settings and policies are protected from prying eyes. To provide this protection, iOS allows you to encrypt profiles so that they can be read only by a single device.

An encrypted profile is just like a normal configuration profile except that the configuration profile payload is encrypted with the public key associated with the device’s X.509 identity.

To keep adversaries from modifying the content, the encrypted configuration profile is signed by the service. For encryption and signing, iOS uses the Cryptographic Message Syntax (CMS), a standard that is also used in S/MIME. Payloads are encrypted using PKCS#7 enveloped data. Profiles are signed using PKCS#7 signed data.

The steps in the device configuration phase are:

1. The device sends a signed request for the `/profile` handler again to request the final profile. (The request is signed with the identity certificate obtained in the previous step.)

   For a sample profile for this phase, see [Sample Phase 4 Device Response](Configuration%20Profile%20Examples.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tkmbvfvbuqnbnknlto).
2. The server’s profile request handler (described in [Profile Request (/profile) URL Handler](Creating%20a%20Profile%20Server%20for%20Over-The-Air%20Enrollment%20and%20Configuration.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tkmbvfvbuqmrnknltenq)) sends the final encrypted profile to the device.

Upon receiving the final encrypted profile, the device installs it. Reconfiguration occurs automatically if the profile expires or if a VPN connection attempt fails.

Settings enforced by a configuration profile cannot be changed on the device. To change these settings, you must install an updated profile.

Configuration profile updates are not pushed to users automatically. If you need to make other profile updates without waiting for the profiles to expire, you must distribute them manually or require users to re-enroll. (Devices also pull new profiles upon a VPN authentication failure.)

You can distribute updated profiles to your users in an email attachment or a webpage. To update a profile, the following conditions must be met:

- The profile identifier must match.

  For more information about the identifier, see [Configuration Profile Examples](Configuration%20Profile%20Examples.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tkmbvfvbuqnbnknltc).
- If the profile was signed, the replacement profile must also be signed by the same issuer.

Depending on the General Settings payload you specified when creating the profile, it may be possible for the user to remove the profiles.

- If the profile requires a password for removal, the user is prompted for that password upon tapping Remove.
- If the profile specifies that it cannot be removed by the user, the Remove button does not appear.

For more information about profile security settings, see [Configuration Profile Examples](Configuration%20Profile%20Examples.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tkmbvfvbuqnbnknltc).

[Next](Creating%20a%20Profile%20Server%20for%20Over-The-Air%20Enrollment%20and%20Configuration.md)[Previous](Introduction.md)

