---
title: Over-the-Air Profile Delivery and Configuration
apple_id: TP40009505
resource_type: Guide
platform: iOS
topic: null
technology: null
published: '2018-04-09'
source_url: https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/iPhoneOTAConfiguration/profile-service/profile-service.html
archived_at: '2026-07-18T01:33:26.900441Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Over-the-Air Profile Delivery and Configuration](Introduction.md)


[Next](Configuration%20Profile%20Examples.md)[Previous](Over-the-Air%20Profile%20Delivery%20Concepts.md)

# Creating a Profile Server for Over-The-Air Enrollment and Configuration

When creating a profile server, you must perform several steps:

1. Configure your infrastructure. This is described in [Configuring the Infrastructure](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tkmbvfvbuqmrnknltgny).
2. Obtain an SSL Certificate for your server. This is described in [Obtaining an SSL Certificate](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tkmbvfvbuqmrnknltgnq).
3. Create a template configuration profile. This is described in [Creating A Template Configuration Profile](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tkmbvfvbuqmrnknltg).
4. Create the server code. The pieces of a server are described in [Starting the Server](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tkmbvfvbuqmrnknltq) and [Profile Service Handlers](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tkmbvfvbuqmrnknltcmy).
5. Add appropriate authentication specific to your environment.
6. Test the service.

The sections that follow take you through the various parts of the profile delivery service source code.

Implementing over-the-air enrollment and configuration requires you to integrate authentication, directory, and certificate services. The process can be deployed using standard web services, but you must set up several key systems ahead of time.

For user authentication, you can use basic HTTP authentication or integrate authentication with your existing directory services. Regardless of the services used, you will need to provide a web-based authentication method for your users to request enrollment.

The process of enrollment requires deployment of standard x.509 identity certificates to iOS users. To do this, you will need a CA (certificate authority) to issue the device credentials using the Simple Certificate Enrollment Protocol (SCEP).

Cisco IOS and Microsoft Server 2003 (with the add-on for certificate services) both support SCEP. There are also a number of hosted PKI services that support SCEP, such as Verisign, Entrust, and RSA. For links to PKI, SCEP, and related topics read the [See Also](Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tkmbvfvbuqmjnknltg) section in [Introduction](Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tkmbvfvbuqmjnknltc).

To implement this process you will need to develop a profile service, which is an HTTP-based daemon that manages iOS-based device connections throughout the process, generates configuration profiles for the user, and verifies user credentials along the way.

There are a few key functions that the profile service needs to provide:

- Host a user-accessible website to support the HTTPS session
- Authenticate incoming user requests using a web-based authentication method (basic, or integrated with directory services)
- Generate the necessary configuration profiles (XML format) depending on the phase of the process
- Sign and encrypt configuration profiles using public key cryptography
- Track the user through the steps in the process (via timestamp and logging methods)
- Manage connections to the certificate authority or directory services

The first step in setting up a profile service is to obtain or generate an SSL certificate for the web server. When hosting a profile server, each iOS-based device must be able to make a secure connection to the server. The easiest way to do this is to get an SSL certificate from a public CA that is already trusted by iOS. For a complete list, see [Lists of Available Trusted Root Certificates in iOS](https://support.apple.com/en-us/HT204132).

Alternatively, you can generate your own root certificate and self-sign it, though if you do, the user will be asked whether they trust the certificate.

The profile service uses a template configuration profile as the starting point, then modifies the profile for a specific device. You must create this template ahead of time and save it to a file on disk. The Apple Configurator provides an easy means of creating a base profile.

In addition to general settings, this configuration profile should also define enterprise policies that you want to enforce. For company-owned equipment, it should be a locked profile to prevent the user from removing it from the device.

For more information about these profiles, read [Configuration Profile Reference](https://developer.apple.com/library/archive/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1).

After you have an SSL certificate, you must configure a web server to host your profile service and an SCEP-aware certificate authority to issue certificates.

The initialization function, `init`, loads the HTTP server’s certificate and private SSL key. These keys and certificates are stored on disk for reuse together with the serial number of the last issued certificate. This function is shown in Listing 2-1.

__Listing 2-1__  Starting the web server

```
world = WEBrick::HTTPServer.new(
  :Port            => 8443,
  :DocumentRoot    => Dir::pwd + "/htdocs",
  :SSLEnable       => true,
  :SSLVerifyClient => OpenSSL::SSL::VERIFY_NONE,
  :SSLCertificate  => @@ssl_cert,
  :SSLPrivateKey   => @@ssl_key
)
```

This example starts the server on port `8443` so it does not have to run as root. The `:DocumentRoot` value should contain the path of an empty directory inside the profile service directory.

You should enable SSL and set the values of `SSLCertificate` and `SSLPrivateKey` to point to your actual SSL certificate and key that you obtained in [Obtaining an SSL Certificate](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tkmbvfvbuqmrnknltgnq).

You should also disable client certificate authentication because the client device does not have a verifiable identity yet.

After you have a basic web server, you need to write handlers for several pages used in the enrollment and delivery process.

The welcome page is the first page new users see when they enter the site at the root level (`/`). A handler for this page is shown in Listing 2-2.

__Listing 2-2__  Handler for `/` URL

```
world.mount_proc("/") { |req, res|
    res['Content-Type'] = "text/html"
    res.body = <<WELCOME_MESSAGE

<style>
body { margin:40px 40px;font-family:Helvetica;}
h1 { font-size:80px; }
p { font-size:60px; }
a { text-decoration:none; }
</style>

<h1 >ACME Inc. Profile Service</h1>

<p>If you had to accept the certificate accessing this page, you should
download the <a href="/CA">root certificate</a> and install it so it becomes trusted.

<p>We are using a self-signed
certificate here, for production it should be issued by a known CA.

<p>After that, go ahead and <a href="/enroll">enroll</a>

WELCOME_MESSAGE

}
```

If you used a self-signed certificate above, when the user goes to this page, Safari asks whether you want to trust the server’s SSL certificate. Agreeing allows you to view the page. This is not sufficient for enrollment, however.

Regardless of whether the site certificate is self-signed or not, the enrollment process with the SCEP service also requires the device to trust the custom certificate authority’s root certificate, which means adding the CA root certificate to the device’s trusted anchors list. To do this, you must create a URL handler that provides the certificate with the correct MIME type.

The link to `/CA` in the welcome page provides a means for the user to add the custom certificate authority’s root certificate to the device’s trusted anchors list. This is required for the SCEP stage of the enrollment process.

After Safari on iOS loads the root certificate from that URL, it asks the user for permission to add the new root certificate to the device’s trusted anchors list. (You should access this page only over a secure connection.)

The handler in Listing 2-3 sends the root certificate.

__Listing 2-3__  Handler for `/CA` URL

```
world.mount_proc("/CA") { |req, res|
    res['Content-Type'] = "application/x-x509-ca-cert"
    res.body = @@root_cert.to_der
}
```

After the user has downloaded the root certificate from a trusted web server over HTTPS, the user can click to continue the enrollment process.

Listing 2-4 provides a handler for the `/enroll` link on the welcome page.

__Listing 2-4__  Handler for `/enroll` URL

```
world.mount_proc("/enroll") { |req, res|
    HTTPAuth.basic_auth(req, res, "realm") {|user, password|
        user == 'apple' && password == 'apple'
    }

    res['Content-Type'] = "application/x-apple-aspen-config"
    configuration = profile_service_payload(req, "signed-auth-token")
    signed_profile = OpenSSL::PKCS7.sign(@@ssl_cert, @@ssl_key,
            configuration, [], OpenSSL::PKCS7::BINARY)
    res.body = signed_profile.to_der

}
```

The handler above performs very limited authentication to identify the user. The user logs in by sending the word `apple` as the user name and password over a connection authenticated with HTTP basic authentication. In a production server environment, you should instead tie this code into a directory service or some other account system.

This handler sets the MIME type of its response to `application/x-apple-aspen-config`, so Safari on iOS treats the response as a configuration profile.

The `profile_service_payload` function ([Profile Service Payload](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tkmbvfvbuqmrnknlti)) produces a special configuration that tells the phone to enroll itself in the profile service. The literal string `"signed-auth-token"` should be replaced with an authorization token from the authentication service that verified the user’s credentials.

Finally, this function signs the profile by calling `OpenSSL::PKCS7.sign` and sends the signed profile to the device.

The first payload sent to the device (after establishing that it is allowed to enroll) is the profile service payload. This payload is sent by a call to `profile_service_payload(req, "signed-auth-token")` from the `/enroll` handler (Listing 2-4).

For a sample profile service payload, see [Sample Phase 1 Server Response](Configuration%20Profile%20Examples.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tkmbvfvbuqnbnknlti).

__Listing 2-5__  `profile_service_payload` function

```
def profile_service_payload(request, challenge)
    payload = general_payload()

    payload['PayloadType'] = "Profile Service" # do not modify
    payload['PayloadIdentifier'] = "com.acme.mobileconfig.profile-service"

    # strings that show up in UI, customisable
    payload['PayloadDisplayName'] = "ACME Profile Service"
    payload['PayloadDescription'] = "Install this profile to enroll for secure access to ACME Inc."

    payload_content = Hash.new
    payload_content['URL'] = "https://" + service_address(request) + "/profile"
    payload_content['DeviceAttributes'] = [
        "UDID",
        "VERSION"
=begin
        "PRODUCT",              # e.g. iPhone1,1 or iPod2,1
        "SERIAL",               # The device's serial number
        "MEID",                 # The device's Mobile Equipment Identifier
        "IMEI"
=end
        ];
    if (challenge && !challenge.empty?)
        payload_content['Challenge'] = challenge
    end

    payload['PayloadContent'] = payload_content
    Plist::Emit.dump(payload)
end
```

This function starts by calling `general_payload`, which sets the version and organization (these values don’t change on a given server) and returns a template payload that provides a UUID for the profile.

The payload content provides a URL where the device should send its identification (using HTTP POST), along with a list of attributes that the server expects the device to provide (software version, IMEI, and so on).

If an authorization token (representing a user authentication) is passed in from the caller (shown in [Listing 2-4](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tkmbvfvbuqmrnknltc)), that token is added as the `Challenge` attribute.

In response, the device sends back the list of requested attributes along with their values. If the server sent a `Challenge` value in its request, the device also includes this value along with the requested device attributes. Finally, to prove it is an iOS-based device, the device signs this identification with its device certificate. This response is sent to the handler for the `/profile` URL.

Validate that the device certificate is issued from “Apple iPhone Device CA”, which has the following Base64 encoded PEM data:

```
-----BEGIN CERTIFICATE----- MIIDaTCCAlGgAwIBAgIBATANBgkqhkiG9w0BAQUFADB5MQswCQYDVQQGEwJVUzET MBEGA1UEChMKQXBwbGUgSW5jLjEmMCQGA1UECxMdQXBwbGUgQ2VydGlmaWNhdGlv biBBdXRob3JpdHkxLTArBgNVBAMTJEFwcGxlIGlQaG9uZSBDZXJ0aWZpY2F0aW9u IEF1dGhvcml0eTAeFw0wNzA0MTYyMjU0NDZaFw0xNDA0MTYyMjU0NDZaMFoxCzAJ BgNVBAYTAlVTMRMwEQYDVQQKEwpBcHBsZSBJbmMuMRUwEwYDVQQLEwxBcHBsZSBp UGhvbmUxHzAdBgNVBAMTFkFwcGxlIGlQaG9uZSBEZXZpY2UgQ0EwgZ8wDQYJKoZI hvcNAQEBBQADgY0AMIGJAoGBAPGUSsnquloYYK3Lok1NTlQZaRdZB2bLl+hmmkdf Rq5nerVKc1SxywT2vTa4DFU4ioSDMVJl+TPhl3ecK0wmsCU/6TKqewh0lOzBSzgd Z04IUpRai1mjXNeT9KD+VYW7TEaXXm6yd0UvZ1y8Cxi/WblshvcqdXbSGXH0KWO5 JQuvAgMBAAGjgZ4wgZswDgYDVR0PAQH/BAQDAgGGMA8GA1UdEwEB/wQFMAMBAf8w HQYDVR0OBBYEFLL+ISNEhpVqedWBJo5zENinTI50MB8GA1UdIwQYMBaAFOc0Ki4i 3jlga7SUzneDYS8xoHw1MDgGA1UdHwQxMC8wLaAroCmGJ2h0dHA6Ly93d3cuYXBw bGUuY29tL2FwcGxlY2EvaXBob25lLmNybDANBgkqhkiG9w0BAQUFAAOCAQEAd13P Z3pMViukVHe9WUg8Hum+0I/0kHKvjhwVd/IMwGlXyU7DhUYWdja2X/zqj7W24Aq5 7dEKm3fqqxK5XCFVGY5HI0cRsdENyTP7lxSiiTRYj2mlPedheCn+k6T5y0U4Xr40 FXwWb2nWqCF1AgIudhgvVbxlvqcxUm8Zz7yDeJ0JFovXQhyO5fLUHRLCQFssAbf8 B4i8rYYsBUhYTspVJcxVpIIltkYpdIRSIARA49HNvKK4hzjzMS/OhKQpVKw+OCEZ xptCVeN2pjbdt9uzi175oVo/u6B2ArKAW17u6XEHIdDMOe7cb33peVI6TD15W4MI pyQPbp8orlXe+tA8JA== -----END CERTIFICATE-----
```


The handler for the `/profile` URL is called twice—once to send the device authentication request before the device is allowed to enroll using SCEP, then again after the SCEP step to deliver the final profile to the device.

In this handler, the profile server receives a PKCS#7 signed data payload from the device, which it then unpack and verifies. For a sample of this profile, see [Sample Phase 2 Device Response](Configuration%20Profile%20Examples.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tkmbvfvbuqnbnknltk).

To make it easier to follow, the `/profile` handler is divided into smaller pieces. The first piece of this handler is shown in Listing 2-6.

__Listing 2-6__  Handler for `/profile` URL, part 1 of 7

```
world.mount_proc("/profile") { |req, res|

    # verify CMS blob, but don't check signer certificate
    p7sign = OpenSSL::PKCS7::PKCS7.new(req.body)
    store = OpenSSL::X509::Store.new
    p7sign.verify(nil, store, nil, OpenSSL::PKCS7::NOVERIFY)
    signers = p7sign.signers
```

If the device signed the request with a certificate that belongs to the hierarchy that issues profile service identities (that is, if this device has enrolled previously), execution follows the first path (shown in Listing 2-7). This path either issues an updated encrypted configuration or, as implemented here, redirects the device to enroll again. For testing purposes, any device that has gotten a profile previously must reenroll.

__Listing 2-7__  Handler for `/profile` URL, part 2 of 7

```
    # this should be checking whether the signer is a cert we issued
    #
    if (signers[0].issuer.to_s == @@root_cert.subject.to_s)
        print "Request from cert with serial #{signers[0].serial}"
            " seen previously: #{@@issued_first_profile.include?(signers[0].serial.to_s)}"
            " (profiles issued to #{@@issued_first_profile.to_a}) \n"
        if (@@issued_first_profile.include?(signers[0].serial.to_s))
          res.set_redirect(WEBrick::HTTPStatus::MovedPermanently, "/enroll")
            print res
```

By this point, any previously fully enrolled clients have been redirected to the enrollment page to enroll again.

If the code gets past this step, it has received either a list of properties or a new request for a final profile.

In Listing 2-8, the encrypted profile is generated. Because this is part of phase 3 (device configuration), it is included here without further comment, and is explained further in [The /profile Handler Revisited](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tkmbvfvbuqmrnknltcnq).

__Listing 2-8__  Handler for `/profile` URL, part 3 of 7

```
        else
            @@issued_first_profile.add(signers[0].serial.to_s)
            payload = client_cert_configuration_payload(req)
                        # vpn_configuration_payload(req)

            #File.open("payload", "w") { |f| f.write payload }
            encrypted_profile = OpenSSL::PKCS7.encrypt(p7sign.certificates,
                payload, OpenSSL::Cipher::Cipher::new("des-ede3-cbc"),
                OpenSSL::PKCS7::BINARY)
            configuration = configuration_payload(req, encrypted_profile.to_der)
        end
```

The code in Listing 2-9 handles the case where the device sent its identification. This part should ideally verify that the response was signed with a valid device certificate and should parse the attributes.

__Listing 2-9__  Handler for `/profile` URL, part 4 of 7

```
    else
        #File.open("signeddata", "w") { |f| f.write p7sign.data }
        device_attributes = Plist::parse_xml(p7sign.data)
        #print device_attributes
```

The next bit of code, Listing 2-10, is commented out with `=begin` and `=end`. It shows how you can restrict issuance of profiles to a single device (by its unique device ID, or UDID) and verify that the `Challenge` is the same as the `Challenge` value issued previously.

In a production environment, this is typically replaced by site-specific code that queries a directory service to validate the authorization token and queries a database of authorized UDID values for devices owned by your organization.

__Listing 2-10__  Handler for `/profile` URL, part 5 of 7

```

=begin
        # Limit issuing of profiles to one device and validate challenge
        if device_attributes['UDID'] == "213cee5cd11778bee2cd1cea624bcc0ab813d235" &&
            device_attributes['CHALLENGE'] == "signed-auth-token"
        end
=end
```

Next, the snippet in Listing 2-11 obtains a payload to send to the device that will tell it how to complete the enrollment process. The details of this configuration are described in the discussion of `encryption_cert_payload`.

__Listing 2-11__  Handler for `/profile` URL, part 6 of 7

```
        configuration = encryption_cert_payload(req, "")
    end
```

Finally, if this function has nothing to send, it raises an exception that makes the http request fail. Otherwise it signs the profile to be sent and returns it. These bits of code are shown in [Listing 2-12](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tkmbvfvbuqmrnknlteny).

__Listing 2-12__  Handler for `/profile` URL, part 7 of 7

```
    if !configuration || configuration.empty?
        raise "you lose"
    else
   	# we're either sending a configuration to enroll the profile service cert
   	# or a profile specifically for this device
   	res['Content-Type'] = "application/x-apple-aspen-config"

        signed_profile = OpenSSL::PKCS7.sign(@@ssl_cert, @@ssl_key,
            configuration, [], OpenSSL::PKCS7::BINARY)
        res.body = signed_profile.to_der
        File.open("profile.der", "w") { |f| f.write signed_profile.to_der }
    end
}
```

After this function sends the configuration to tell the device how to enroll, the device enrolls its identity using SCEP. Then, it sends a request for the `/profile` URL associated with this handler a second time to obtain the final profile.

The actual payload is described in [Configuration Profile Payload](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tkmbvfvbuqmrnknltm) and [Encryption Certificate Payload](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tkmbvfvbuqmrnknlto). For a sample configuration profile, see [Sample Phase 3 Server Response With SCEP Specifications](Configuration%20Profile%20Examples.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tkmbvfvbuqnbnknltm).

Previously, [Listing 2-8](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tkmbvfvbuqmrnknltcoi) showed the encrypted profile generation process. The code in question doesn’t actually run until phase 3, however, so the details were deferred. This section revisits that section of the `/profile` handler and provides explanation.

The encrypted profile is generated as follows:

- A configuration is generated with a set of configuration payloads. (See [Configuration Profile Reference](https://developer.apple.com/library/archive/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206-CH1) to learn about the contents of these payloads in detail.)

  In this reference implementation, every device gets the same profile. If desired, however, the `Challenge` information can be used to identify the user requesting the profile, and the code can generate a profile specific to that user.

  Similarly, the device information provided can be used to generate a profile specific to a given device or a particular type of device (for example, providing a different profile for different iOS-based device models).
- The configuration is encrypted with the public key of the device that signed the original request.
- The encrypted blob of data is wrapped in a configuration profile.

The details of this encrypted blob are explained in the descriptions of `client_cert_configuration_payload` ([Listing A-1](Configuration%20Profile%20Examples.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tkmbvfvbuqnbnknltcoa)) and `configuration_payload` ([Configuration Profile Payload](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tkmbvfvbuqmrnknltm)).

__Listing 2-13__  Handler for `/profile` URL, part 3 of 7 (revisited)

```
        else
            @@issued_first_profile.add(signers[0].serial.to_s)
            payload = client_cert_configuration_payload(req)
                        # vpn_configuration_payload(req)

            #File.open("payload", "w") { |f| f.write payload }
            encrypted_profile = OpenSSL::PKCS7.encrypt(p7sign.certificates,
                payload, OpenSSL::Cipher::Cipher::new("des-ede3-cbc"),
                OpenSSL::PKCS7::BINARY)
            configuration = configuration_payload(req, encrypted_profile.to_der)
        end
```


The configuration profile payload (provided by `configuration_payload`) resembles the profile service payload described in [Profile Service Payload](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tkmbvfvbuqmrnknlti). The only difference is in the payload its carries.

For a sample profile for this phase, see [Sample Phase 4 Device Response](Configuration%20Profile%20Examples.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tkmbvfvbuqnbnknlto).

Listing 2-14 describes the encryption certificate payload. This payload tells the client how to complete the enrollment process.

__Listing 2-14__  `encryption_cert_payload` function

```
def encryption_cert_payload(request, challenge)
    payload = general_payload()

    payload['PayloadIdentifier'] = "com.acme.encrypted-profile-service"
    payload['PayloadType'] = "Configuration" # do not modify

    # strings that show up in UI, customisable
    payload['PayloadDisplayName'] = "Profile Service Enroll"
    payload['PayloadDescription'] = "Enrolls identity for the encrypted profile service"

    payload['PayloadContent'] = [scep_cert_payload(request, "Profile Service", challenge)];
    Plist::Emit.dump(payload)
end
```

The `scep_cert_payload` function is described in [SCEP Certificate Payload](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tkmbvfvbuqmrnknltk).

As the name of the `scep_cert_payload` function suggests, the function shown in Listing 2-15 produces an SCEP payload that gives the device the information it needs to enroll a certificate.

__Listing 2-15__  `scep_cert_payload` function

```
def scep_cert_payload(request, purpose, challenge)
    payload = general_payload()

    payload['PayloadIdentifier'] = "com.acme.encryption-cert-request"
    payload['PayloadType'] = "com.apple.security.scep" # do not modify
```

The payload type of `com.apple.security.scep` indicates an SCEP payload and the content specifies the parameters.

```
    # strings that show up in UI, customisable
    payload['PayloadDisplayName'] = purpose
    payload['PayloadDescription'] = "Provides device encryption identity"

    payload_content = Hash.new
    payload_content['URL'] = "https://" + service_address(request) + "/scep"
```

First and foremost, there is the base URL for the SCEP service, which for convenience is handled by the sample service as well. It looks a little different for IOS (`http://scep-server/cgi-bin/pkiclient.exe`) and Windows SCEP servers (`http://scep-server/certsrv/mscep/mscep.dll`).

```
=begin
    # scep instance NOTE: required for MS SCEP servers
    payload_content['Name'] = ""
=end
```

The service can provide different certificate issuing services parameterized on the `Name` value that becomes part of the final URL. In the case of Windows, this value needs to be set, although any value will do.

```
    payload_content['Subject'] = [ [ [ "O", "ACME Inc." ] ],
        [ [ "CN", purpose + " (" + UUIDTools::UUID.random_create().to_s + ")" ] ] ];
    if (!challenge.empty?)
        payload_content['Challenge'] = challenge
    end
```

The subject allows the client to specify the requested subject. In this case, it is populated by the profile service. Some services may not want to grant the client the ability to specify it, and may use the `Challenge` to encode the identity of the requester.

X.509 subjects are elaborate structures and are mimicked here as an array of arrays, to fully specify it. Each key-value pair is specified as an array. The key is the first element and is a string with a value that is either an ID (for example, "0.9.2342.19200300.100.1.25" is DC) or one of the recognized abbreviations (CN, C, ST, L, O, OU). The example above represents a subject that will often be displayed as "/O=ACME Inc./CN={purpose} ({random UUID})".

```
    payload_content['Keysize'] = 1024
```

Next up are some, simple parameters, although they require some consideration. Key size requests the device to generate a keypair of a certain size. Only 1024-bit and 2048-bit key sizes should be used. Keys larger than 2048 bits are not supported. In general, 1024-bit keys are recommended because of the overhead involved in generating 2048-bit keys.

```
    payload_content['Key Type'] = "RSA"
```

The key type should always be RSA because this reference implementation (and in practice, SCEP) only support RSA keys.

```
    payload_content['Key Usage'] = 5 # digital signature (1) | key encipherment (4)
```

Key usage specifies the purposes the key can be used for and is a bit mask. Bit 0 (value 1) specifies digital signature, and bit 2 specifies key encipherment. Note that the MS SCEP server will only issue signature or encryption, not both.

```
=begin
    payload_content['CAFingerprint'] = StringIO.new(OpenSSL::Digest::SHA1.new(@@root_cert.to_der).digest)
=end
```

SCEP can run over HTTP, as long as the CA cert is verified out of band. This functionality is currently disabled (as shown above) because iOS does not currently support this. This function supports such operation by adding the fingerprint to the SCEP payload that the phone downloads over HTTPS during enrollment, as shown below:

```
    payload['PayloadContent'] = payload_content;
    payload
end
```

```
            payload = client_cert_configuration_payload(req)
                        # vpn_configuration_payload(req)
```

[Next](Configuration%20Profile%20Examples.md)[Previous](Over-the-Air%20Profile%20Delivery%20Concepts.md)

