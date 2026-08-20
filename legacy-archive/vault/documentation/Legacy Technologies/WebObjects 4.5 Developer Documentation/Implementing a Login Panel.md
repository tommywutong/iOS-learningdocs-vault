---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/Topics/ProgrammingTopics.e.html
archived_at: '2026-07-15T08:10:01.290427Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Programming Topics

[!](WebObjects%20Programming%20Topics.md) [!](Handling%20International%20Character%20Sets%20with%20EOF.md) [!](Generating%20a%20Static%20Site.md)

#   Implementing a Login Panel

##  Synopsis

Describes how to use WebObjects to implement a reusable login panel with the HTTP `Basic' Authorization scheme, how to secure the login connection using SSL, and how to validate a login against a custom database.

##  Discussion

WebObjects applications commonly require authentication code, often in the form of a login panel. This topic implements a login panel class that you can subclass and use in your applications.

WebObjects login panels can be implemented in the following ways:

- 

  Using a basic HTML page with a login form containing text fields and a Submit button
- 

  Using the HTTP/1.x Basic authentication protocol with the browser's built-in authentication panel

Creating a login form using HTML is very easy but suffers two disadvantages: the login credentials are sent in clear text all the way to the application server, and the page's HTML requires maintenance. HTTP-based access authentication uses a browser's login panel to capture the users login information and encodes (but does not encrypt) the login credentials all the way to the application server. Combining either of these login approaches with a secure connection between the browser and the HTTP server using SSL yields a very secure login solution.

This programming topic implements a login using the HTTP 1.x Basic authentication scheme, specified in the HTTP/1.0 and HTTP/1.1 standards. The implementation has two phases: presentation and validation. Presentation involves implementing the HTTP/1.x Basic Authentication scheme, decoding the user's login credentials, and presenting an error response if the login fails. Validation involves validating the user's credentials against a database or authentication server, tracking login attempts, and recording users that have been locked out because they exceeded the maximum number of login attempts.

###  Using HTTP/1.x Basic Authentication

HTTP defines a simple challenge-response authentication protocol: when a client requests a secure document, the server challenges the client, whereupon the client supplies his credentials, i.e., a user ID and a password. The documents are organized in "realms". Once the user is permitted to access a particular realm, his browser will cache the login credentials and respond automatically and transparently to further challenges by the server. The authentication realm can have the following values:

|  |  |
| --- | --- |
|   Realm Value |   Authentication Space |
|   Application Name |   Authenticated one for all application sessions. |
|   sessionID |   Authenticated for a single application session. |
|   Page Name |   Authenticated for a particular page in all sessions. |
|   SessionID+Page Name |   Authenticated for a particular page in one session. |
|   ContextId |   Authenticated for one request only. |

!Note Once the user exits the browser, all of his authenticated realms are lost because
the browser forgets his username and password.!

The state of the authentication process is stored in the
session
object using the
authState
variable. Table 1 shows the authentication request-response loop:

__

Request-Response Loop__|   Browser |   Current Page |   Authenticated Page |
|   Submits request for authenticated page.    Brings up login panel if realm was not previously authenticated.    Sets authorization header to include the encoded login information and sends authorization request.    Displays Authenticated page.    Displays Error page. |   Invokes requested method to create page.    Creates new Authenticated page.    Sets new page's  authState variable to  "authNeeded" .    Returns Authenticated page with modified content and HTTP status.    Receives same request to invoke method.    Creates or returns new Authenticated page.    Returns normal Authenticated page with HTTP status 200.    Returns Authenticated page with error content and HTTP 403 status. |   Overrides  appendToResponse , invokes super.appendToResponse , then invokes  handleAuthorizationRequest    If  authState = "authNeeded" , sets HTTP status to 401, sets the response header to indicate the realm, and sets  authState to  "authLogin" .    If  authState = "authLogin" , decode and parse encoded login string and perform validation. Sets  authState  to "accessDenied" or  "authenticated" .    If  authState = "authenticated" , generates normal response page .    If  authState = "accessDenied" , sets HTTP status to 403 and content to HTTP 403(Unauthorized) |

When your application receives a request for a specific page, or a method invocation in the current page, it can challenge the request by sending a special response that causes the browser to display the authentication panel.

###  An Example

This application has two pages, implemented in Listings 1 and 2. The
Main
page is a welcome page with a link to login and continue. The second page is the page containing secure data. In
Main
,
anAction()
is invoked when the user's request to login is received. This method creates the new page, a subclass of
AuthenticatedComponent
, that displays the login panel and validates the login. Once the login is validated, the page returns its normal contents. In Listing 1, the
page.authenticateComponent()
message flags that
page
requires authentication. The login panel is displayed when
page
is returned.

####  Java Code for the Main Page

```

public class Main extends WOComponent {
    public WOComponent anAction()
    {
        AuthenticatedComponent page;
        page=(AuthenticatedComponent)this.pageWithName("NewPage");
        page.authenticateComponent(this.session().sessionID());
        return page;
    }
}
//NewPage.java code fragment
public class NewPage extends AuthenticatedComponent {. . . . . .
```


When
page.authenticateComponent()
is invoked, the
authState
variable is set to
"authNeeded"
and is stored in the session dictionary along with
authSpace
. In this example
authSpace
contains the authentication realm; it is set to the
sessionID
to indicate that authentication is only required once per session.

####  Java Code for the Secure Page

```

public class AuthenticatedComponent extends WOComponent{
public void authenticateComponent(String authSpace){
    String authState=(String)this.session().objectForKey("authState");
    if(authState==null){
        this.session().setObjectForKey("authNeeded","authState");
        this.session().setObjectForKey(authSpace,"authSpace");
    }
...
```


The
appendToResponse()
method, invoked automatically when a page is returned, is overridden to display the login panel. For clarity, this example implements the guts of the response generator in a separate method:
responseForAuthorization(WOResponse aResponse, String aRealm ),
where parameter
aRealm
refers to the protection space. The superclass version of
appendToResponse()
must be called first to generate the initial WOResponse.

####  Java Code for Overriding appendToResponse

```

// in the AuthenticatedComponent class

public void appendToResponse(WOResponse aResponse, WOContext aContext)
{
    String sessionId;
    super.appendToResponse(aResponse, aContext);
    sessionId=(String)this.session().objectForKey("authSpace");
    responseForAuthorization(aResponse, sessionId);
}
```


Listing 4 shows the
responseForAuthorization
code which actually generates the response. If the
authState
is
"authNeeded"
, the response is initialized with the HTTP status set to 401. The
WWW-Authenticate
header is set with the value
Basic realm="some sessionID"
. When the browser receives this response, it pops up a login panel requesting the user ID and password. When the user enters this information, the browser sends it back to the web server along with the original request. This request contains an
Authorization
header and the
<Base64 encoded>
credentials having the format:
Basic <userid:password>.

If the validation is unsuccessful,
responseForAuthorization
returns a response with HTTP status 403 (Unauthorized). If the validation is successful,
responseForAuthorization
returns the response page unmodified. You can add code to handle users that attempt to login too many times. Possible strategies are:

- 

  Terminate the session after the 403 response is sent by invoking

  WebApplication.session().terminate();
  The session will terminate after the response is sent.
- 

  Record the remote user's IP address and disallow further login attempts from this IP address for a limited time. You can get the IP address of the remote host by reading the value of the
  x-webobjects-remote-host
  header from the request, then terminate the session.

####  Java Code for responseForAuthorization

```

String ipAddr=aRequest.headerForKey("x-webobjects-remote-host");

//In AuthenticatedComponent
public void responseForAuthorization(WOResponse aResponse,String aRealm )
{
    NSData errorBytes;
    String errorText=
        "<HTML><BODY><H2>HTTP/1.0 403 Unauthorized Access</H2></BODY></HTML>";
    String authState=(String)this.session().objectForKey("authState");
    if(authState!=null  )
    {
        String encodedAuth=this.context().
            request().headerForKey("authorization");

        if(encodedAuth!=null && authState.equals("authLogin"))
        {
            handleAuthorizationRequest(encodedAuth);
            authState=(String)this.session().objectForKey("authState");
        }

        if(authState.equals("authenticated"))
            return;
        else
        {
            errorBytes = new NSData(errorText.getBytes());
            aResponse.setContent(errorBytes);
            aResponse.setHeader(new Integer(errorBytes.length()).
                toString(), "content-length");
            aResponse.setHeader("text/html" , "content-type");
            if(authState.equals("authNeeded")  )//validation needed
            {
                aResponse.setStatus(401); //authorization request
                aResponse.setHeader(
                    "Basic realm=\"" + aRealm + "\"" , "WWW-Authenticate");
                this.session().setObjectForKey("authLogin","authState");
            }
            else if(authState.equals("accessDenied"))
                aResponse.setStatus(403);// unauthorized status
        }
    }
}
```


Listing 5 shows the code that decodes the credentials and invokes the validation code. The authorization header value is extracted from the request and Base64 decoded with
sun.misc.BASE64Decoder
(included with the standard Java Developer Kit (JDK)). The decoded header is parsed to extract the user name and password, which are sent to the validation code.

####  Java Code to Extract Credentials

```

//In AuthenticatedComponent
public  void handleAuthorizationRequest(String encodedAuth)
{
    String decodedAuth=null;
    EOEnterpriseObject validatedUser;
    sun.misc.BASE64Decoder decoder=new sun.misc.BASE64Decoder();

    //encoded string starts after "Basic "
    encodedAuth=encodedAuth.substring(encodedAuth.indexOf(" ")+1);
    try{
        decodedAuth=new String(decoder.decodeBuffer((new ByteArrayInputStream
            (encodedAuth.getBytes()))));
    } catch(IOException ex) {}

    //extract username:password, assume methods and ivars exist
    String userName=userNameFromDecodedAuthString(decodedAuth);
    String password=passwordFromDecodedAuthString(decodedAuth);

    //then validate. Again, assume this exists
    if ((validatedUser=validateUserNameAndPassword(userName,
        password))!=null) {
        this.session().setObjectForKey("authenticated","authState");
        this.session().setObjectForKey(validatedUser,"validatedUser");
    } else {
       this.session().setObjectForKey("authNeeded","authState");
    }
}

public static String userNameFromDecodedAuthString(String auth) {
    if(auth!=null){
        StringTokenizer st=new StringTokenizer(auth,":",true);
        String username;
        if(( username=st.nextToken())!=null){
            if(!username.equals(":")){
                return username;
            }
        }
    }
    return "";
}
public static String passwordFromDecodedAuthString(String auth ) {
    if(auth!=null){
        StringTokenizer st=new StringTokenizer(auth,":",true);
        if(st.countTokens()==3){
            st.nextToken(); st.nextToken();
            return st.nextToken();
        }
        else if(st.countTokens()==2){
            st.nextToken();
            String passwd=st.nextToken();
            if(!passwd.equals(":"))
                return passwd;
        }
    }
    return "";
}
```


###  Implementing Validation

Once the login credentials have been received, decoded, and parsed, they must be validated. Several options exist:

- 

  Authentication on LDAP server
- 

  Custom database with username, password, access rights, and so on
- 

  Create a new database connection with users login credentials.

We discuss the second option, authenticating against a custom database with login information. The following example assumes an existing database with user data and an EOModel. Once the login validation method is invoked, a fetch is performed against the login credentials.

####  Java Code

```

//In AuthenticatedComponent

public EOEnterpriseObject validateUserNameAndPassword
    (String username, String password)
{
    EOQualifier qual;
    EOFetchSpecification fs;
    NSMutableArray args = new NSMutableArray();
    EOEditingContext ec=new EOEditingContext();
    args.addObject(username);
    args.addObject(password);

    qual = EOQualifier.qualifierWithQualifierFormat
        ("userName = %@ AND password = %@", args);
    fs=new EOFetchSpecification("Login", qual, null);
    NSArray im=ec.objectsWithFetchSpecification(fs);

    if(im.count()==1)
        return (EOEnterpriseObject)im.objectAtIndex(0);
    return null;
}
```


###  How Secure?

Using an HTML or HTTP Authorization login panel by itself does little to protect the login credentials from potential intruders. The login panel based on an HTML form is the least secure, offering no real protection except the ability to hide the user's password on the screen, because the login information is sent in clear text all the way back to the WebObjects application server.

Using the browser authentication panel, login information is Base64 encoded all the way to the WebObjects application server. Although safer than clear text, it is easily decoded.

Using the Secure Socket Layer (SSL) with either of these login approaches yields an excellent and secure Web application login solution. Even with SSL, the login credentials remain unencrypted between the HTTP server and WebObjects application server. However, this link is usually highly secure, especially if it's behind a firewall.

###  Securing the Login with SSL

To get a secure connection between the browser and the HTTP server using SSL, two things are needed:

- 

  An HTTP server "Security Certificate" signed by a Certificate Authority (CA) such as Verisign
- 

  Redirection of the URL by modifying the URL prefix from
  http://
  to
  https://

To redirect the URL, you must modify the location header of the response in the appendToResponse method of the page, session, or application:

```

rsp.setHeader("https://"+this.context().request().headerForKey("host")+this.context().componentActionURL(), "location");
```


To make the connection insecure after the login is complete, you can do the following:

```

rsp.setHeader("http://"+this.context().request().headerForKey("host")+this.context().componentActionURL(), "location");
```


These methods should be placed in
responseForAuthorization()
.

###  Caveats

Netscape HTTP servers will not pass the Authorization header to Common Gateway Interface (CGI) programs; you must use the NSAPI adapter included with WebObjects. Microsoft IIS servers must be configured for "Basic Authentication." Microsoft Peer Web Server does not directly support "Basic Authentication," but can be made to work by making the following registry entry in:

HKEY_LOCAL_MACHINE/SYSTEM/CurrentControlSet/Services/W3SVC/Parameters

Change NTAuthentication "NTLM" to NTAuthentication "basic" and disable the "Basic Authentication" option in the Internet Service Manager.

##  See Also

- 

  [Fetching with an Editing Context](Fetching%20with%20an%20Editing%20Context.md#apple-ge2tsmzt)

##  Questions

- 

  How do I create a login panel?
- 

  How do I use browser authentication in a WebObjects application?
- 

  How do I implement SSL from a WebObjects application?
- 

  How can I implement a dedicated database connect per user login?

##  Keywords

- 

  Login
- 

  Authentication
- 

  Security

##  Revision History

10 July, 1998. Kelly Kazem. First Draft.

19 November, 1998. Clif Liu. Second Draft.

```

```

---

© 1999 Apple Computer, Inc.

[!](WebObjects%20Programming%20Topics.md) [!](Handling%20International%20Character%20Sets%20with%20EOF.md) [!](Generating%20a%20Static%20Site.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
