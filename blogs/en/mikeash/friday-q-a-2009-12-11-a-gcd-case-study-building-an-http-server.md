---
title: 'Friday Q&A 2009-12-11: A GCD Case Study: Building an HTTP Server'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2009-12-11-a-gcd-case-study-building-an-http-server.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:e69ec3b8b792588b'
translated: false
---

> 原文：[Friday Q&A 2009-12-11: A GCD Case Study: Building an HTTP Server](https://www.mikeash.com/pyblog/friday-qa-2009-12-11-a-gcd-case-study-building-an-http-server.html)　·　mikeash.com Friday Q&A

Posted at 2009-12-11 23:58 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Rogue Amoeba Is Hiring](https://www.mikeash.com/pyblog/rogue-amoeba-is-hiring.html)  
Previous article: [Friday Q&A 2009-12-04: Building Standalone iPhone Web Apps](https://www.mikeash.com/pyblog/friday-qa-2009-12-04-building-standalone-iphone-web-apps.html)  
Tags: [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [gcd](https://www.mikeash.com/pyblog/?tag=gcd) [generators](https://www.mikeash.com/pyblog/?tag=generators) [http](https://www.mikeash.com/pyblog/?tag=http) [networking](https://www.mikeash.com/pyblog/?tag=networking)

Friday Q&A 2009-12-11: A GCD Case Study: Building an HTTP Server

by [Mike Ash](https://www.mikeash.com/)

**Techniques**  
 An HTTP server obviously does a lot of networking, and GCD is great for managing IO. It's quick and easy to set up a dispatch source that triggers when a file descriptor is available for reading and writing, which makes it straightforward to write a server that supports many connections simultaneously without inefficient techniques like using a dedicated thread for each connection, and without having to write your own dispatching loop or deal with messy runloop sources.

The desire for asynchronous IO also makes this a perfect use case for [generators](https://www.mikeash.com/pyblog/friday-qa-2009-10-30-generators-in-objective-c.html). Using a generator allows code to be written in a natural top-down manner while still being completely asynchronous and not occupying a thread until completion. This makes it great for incrementally parsing an HTTP request as it comes down the wire, or incrementally sending the response.

This web server is meant more to illustrate techniques and be easy to understand than to be high performance. The primary source of inefficiency is that it reads and writes a single character at a time, which causes a great deal of overhead, but which simplifies the code substantially. A real server should read and write large buffers at once, and also pass those large buffers to and from the generators in use.

**Source**  
 If you want to follow along at home, the source code [is available in my public subversion repository](http://www.mikeash.com/svn/GCDWeb/GCDWeb.m).

It also depends on [MAGenerator](http://www.mikeash.com/svn/MAGenerator/), so if you want to build it you'll need to build `MAGenerator.m` as well, and make sure that `MAGenerator.h` is in your include path.

Due to the heavy use of generators, you'll need to know what those are and how `MAGenerator` works. If you haven't already, [read my article on `MAGenerator` before you go further](https://www.mikeash.com/pyblog/friday-qa-2009-10-30-generators-in-objective-c.html).

**`main`**  
 I'm going to take a top-down approach to this server, so the logical place to start is `main`. The program is intended to be run with one argument, the port number, so the first thing it does is check for the proper number of arguments, and then extract that port number if it's correct:

```
    int main(int argc, char **argv)
    {
        if(argc != 2)
        {
            fprintf(stderr, "usage: %s <port>\n", argv[0]);
            return 1;
        }
        
        int port = atoi(argv[1]);
```

Next, it will set up sockets to listen on that port (one socket each for IPv4 and IPv6), then call

to let GCD start doing its thing:

```
        SetupSockets(port);
        
        LOG("listening on port %d", port);
        
        dispatch_main();
        
        return 0;
    }
```

The code to set up the sockets is straightforward sockets code, and I won't go into details on that. If you're unfamiliar with sockets, there are lots of references out there. Note that the

macro is just something that tests for a

return value and prints an error and exits the program if so.

```
    static void SetupSockets(int port)
    {
        int listenSocket4 = CHECK(socket(PF_INET, SOCK_STREAM, 0));
        int listenSocket6 = CHECK(socket(PF_INET6, SOCK_STREAM, 0));
        
        struct sockaddr_in addr4 = { sizeof(addr4), AF_INET, htons(port), { INADDR_ANY }, { 0 } };
        struct sockaddr_in6 addr6 = { sizeof(addr6), AF_INET6, htons(port), 0, IN6ADDR_ANY_INIT, 0 };
        
        int yes = 1;
        CHECK(setsockopt(listenSocket4, SOL_SOCKET, SO_REUSEADDR, (void *)&yes, sizeof(yes)));
        CHECK(setsockopt(listenSocket6, SOL_SOCKET, SO_REUSEADDR, (void *)&yes, sizeof(yes)));
        CHECK(bind(listenSocket4, (void *)&addr4, sizeof(addr4)));
        CHECK(bind(listenSocket6, (void *)&addr6, sizeof(addr6)));
        
        SetupListenSource(listenSocket4);
        SetupListenSource(listenSocket6);
    }
```

The

function is where things start to get interesting. This first calls

on the socket to make it start listening for connections. It then creates a new

to handle events on the socket. Note that, just as with

, GCD treats a new connection on a listening socket as a read event, so that's the type of dispatch source that this function creates:

```
    static void SetupListenSource(int s)
    {
        CHECK(listen(s, 16));
        
        dispatch_source_t source = NewFDSource(s, DISPATCH_SOURCE_TYPE_READ, ^{
            AcceptConnection(s);
        });
        dispatch_resume(source);
        
        // leak it, it lives forever
    }
```

The

function is just a simple wrapper for a couple of GCD calls:

```
    static dispatch_source_t NewFDSource(int s, dispatch_source_type_t type, dispatch_block_t block)
    {
        dispatch_source_t source = dispatch_source_create(type, s, 0, dispatch_get_global_queue(0, 0));
        dispatch_source_set_event_handler(source, block);
        return source;
    }
```

When a new connection arrives,

is called to set up the connection. The first thing it does is call

to get the socket for that specific connection:

```
    static void AcceptConnection(int listenSock)
    {
        struct sockaddr addr;
        socklen_t addrlen = sizeof(addr);
        int newSock = CHECK(accept(listenSock, &addr, &addrlen;));
        LOG("new connection on socket %d, new socket is %d", listenSock, newSock);
```

Next, it creates a new

structure:

```
        struct Connection *connection = NewConnection(newSock);
```

I initially thought that I could get away with not having such a structure at all, and let everything about a connection be managed as implicit block/generator state. However, there's a wrinkle. It starts with this text on the

man page:

```
     Important: a cancellation handler is required for file descriptor and
     mach port based sources in order to safely close the descriptor or
     destroy the port. Closing the descriptor or port before the cancellation
     handler has run may result in a race condition: if a new descriptor is
     allocated with the same value as the recently cosed descriptor while the
     source's event handler is still running, the event handler may read/write
     data to the wrong descriptor.
```

The trick is that a socket is bidirectional, and the server will ultimately have _two_ dispatch sources monitoring it, one for reading and one for writing. Neither one can safely close the socket in its cancellation handler, because it's unknown which one will be cancelled first. Thus, the `Connection` structure simply holds the socket as well as a reference count which starts out at 2. Each cancellation handler decrements the refcount, and then closes the socket if it's the last one out.

The next step is to create a request reader, which is a generator that parses the incoming HTTP request:

```
        int (^requestReader)(char) = RequestReader(connection);
```

Next, it creates a dispatch source to look for available data on the new socket. The event handler reads a single character from the socket, then passes that character off to the request reader. On

, it writes out an error response if the request wasn't complete enough to generate a normal response, then cancels the handler. Since this is an HTTP 1.0 server, not a 1.1 server, the connection is not reusable for subsequent requests, but rather the client must open a new one each time.

```
        __block BOOL didSendResponse = NO;
        __block dispatch_source_t source; // gcc won't compile if the next line is an initializer?!
        source = NewFDSource(newSock, DISPATCH_SOURCE_TYPE_READ, ^{
            char c;
            LOG("reading from %d", newSock);
            int howMuch = read(newSock, &c, 1);
            LOG("read from %d returned %d (errno is %d %s)", newSock, howMuch, errno, strerror(errno));
            
            BOOL isErr = NO;
            if(howMuch == -1 && errno != EAGAIN && errno != EINTR)
            {
                LOG("read returned error %d (%s)", errno, strerror(errno));
                isErr = YES;
            }
            if(howMuch > 0)
            {
                int ret = requestReader(c);
                if(ret)
                    didSendResponse = YES;
            }
            if(howMuch == 0 || isErr)
            {
                if(!didSendResponse)
                    Write(connection, ErrCodeWriter(400));
                dispatch_source_cancel(source);
            }
        });
```

Note that after reading a byte, the handler simply falls off the end. As long as data is available, GCD will keep invoking the event handler, so GCD essentially functions as the outer loop to this code.

The cancel handler simply releases the connection and the dispatch source:

```
        dispatch_source_set_cancel_handler(source, ^{
            ReleaseConnection(connection);
            dispatch_release(source);
        });
```

And as its last act,

"resumes" the source so that it can start processing:

```
        dispatch_resume(source);
    }
```

The request reader generator simply accepts a character at a time as a parameter, and parses the HTTP request. The big advantage of using a generator can be seen here, where the parser is written completely top-down, and yet is fully asynchronous. It returns an integer to indicate to the caller whether it sent a response or not, so that the caller can know whether it needs to send its own fail-safe error response. If it hits a parse error at any point, it responds with an error and bails out, otherwise it makes a call to

and tells it which resource it's supposed to process. This parser completely ignores any headers sent by the client, so once the method and resource have been read, it simply enters a loop and skips over any remaining input.

```
    GENERATOR(int, RequestReader(struct Connection *connection), (char))
    {
        NSMutableData *buffer = [NSMutableData data];
        GENERATOR_BEGIN(char c)
        {
            // read the request method
            while(c != '\r' && c != '\n' && c != ' ')
            {
                [buffer appendBytes: &c length: 1];
                GENERATOR_YIELD(0);
            }
            
            // if the line ended before we got a space then we don't understand the request
            if(c != ' ')
            {
                LOG("Got a bad request from the client on %d", connection->sock);
                Write(connection, ErrCodeWriter(400));
                GENERATOR_YIELD(1); // signal that we got enough for a response
            }
            else
            {
                // we only support GET
                if([buffer length] != 3 || memcmp([buffer bytes], "GET", 3) != 0)
                {
                    LOG("Got an unknown method from the client on %d", connection->sock);
                    Write(connection, ErrCodeWriter(501));
                    GENERATOR_YIELD(1); // signal that we got enough for a response
                }
                else
                {
                    // skip over the delimeter
                    GENERATOR_YIELD(0);
                    
                    // read the resource
                    [buffer setLength: 0];
                    while(c != '\r' && c != '\n' && c != ' ')
                    {
                        [buffer appendBytes: &c length: 1];
                        GENERATOR_YIELD(0);
                    }
                    
                    LOG("Servicing request from the client on %d", connection->sock);
                    NSString *s = [[[NSString alloc] initWithData: buffer encoding: NSUTF8StringEncoding] autorelease];
                    if(!s)
                        Write(connection, ErrCodeWriter(400));
                    else
                        ProcessResource(connection, s);
                    GENERATOR_YIELD(1); // signal that we got enough for a response
                }
            }
            
            // we just ignore anything else sent by the client
            while(1)
                GENERATOR_YIELD(0);
        }
        GENERATOR_END
    }
```

The

function is extremely simple. It simply gets a content generator for the resource in question, and writes it:

```
    static void ProcessResource(struct Connection *connection, NSString *resource)
    {
        Write(connection, ContentGeneratorForResource(resource));
    }
```

just checks for known resources and returns the appropriate handler if it finds one, otherwise returning a "not found" handler. If you wanted to add more handlers, this is where they would go:

```
    static NSData *(^ContentGeneratorForResource(NSString *resource))(void)
    {
        if([resource isEqual: @"/"])
            return RootHandler(resource);
        if([resource isEqual: @"/listing"])
            return ListingHandler(resource);
        
        return NotFoundHandler(resource);
    }
```

The

function is basically the inverse of the read handler shown above. It takes the content generator, and wraps it in a byte generator which generates one byte at a time. It then writes those bytes until no more remain, or an error occurs, at which point it shuts down the write side of the socket and releases the connection and dispatch source:

```
    static void Write(struct Connection *connection, NSData *(^contentGenerator)(void))
    {
        int (^byteGenerator)(void) = ByteGenerator(contentGenerator);
        __block dispatch_source_t source;
        source = NewFDSource(connection->sock, DISPATCH_SOURCE_TYPE_WRITE, ^{
            int byte = byteGenerator();
            BOOL err = NO;
            if(byte != -1) // EOF
            {
                unsigned char buf = byte;
                int howMuch;
                do
                {
                    howMuch = write(connection->sock, &buf, 1);
                }
                while(howMuch == -1 && (errno == EAGAIN || errno == EINTR));
                if(howMuch == -1)
                {
                    err = YES;
                    LOG("write returned error %d (%s)", errno, strerror(errno));
                }
            }
            if(byte == -1 || err)
            {
                LOG("Done servicing %d", connection->sock);
                dispatch_source_cancel(source);
            }
        });
        dispatch_source_set_cancel_handler(source, ^{
            CHECK(shutdown(connection->sock, SHUT_WR));
            ReleaseConnection(connection);
            dispatch_release(source);
        });
        dispatch_resume(source);
    }
```

As you can see from the declaration, a content generator is a generator that returns

instances. The idea is that it can return its response in nice manageable chunks, but not have to build up the entire response in memory ahead of time. However, to simplify writing, the server writes only one byte at a time. The

generator takes an

generator and returns the individual bytes, one by one. Since it needs to be able to signal when it reaches the end, it actually returns an

, using

as the

signal and positive numbers for byte values:

```
    GENERATOR(int, ByteGenerator(NSData *(^contentGenerator)(void)), (void))
    {
        __block NSData *data = nil;
        __block NSUInteger cursor = 0;
        GENERATOR_BEGIN(void)
        {
            do
            {
                if(cursor < [data length])
                {
                    const unsigned char *ptr = [data bytes];
                    GENERATOR_YIELD((int)ptr[cursor++]);
                }
                else
                {
                    [data release];
                    data = [contentGenerator() retain];
                    cursor = 0;
                }
            } while(data);
            GENERATOR_YIELD(-1);
        }
        GENERATOR_CLEANUP
        {
            [data release];
        }
        GENERATOR_END
    }
```

With this, the server is essentially complete except for the handlers.

**Resource Handlers**  
 The first handler is an error code writer. Give it a code, it dumps out an appropriate error response. This is used in the request parsing code to handle errors there:

```
    GENERATOR(NSData *, ErrCodeWriter(int code), (void))
    {
        GENERATOR_BEGIN(void)
        {
            if(code == 400)
                GENERATOR_YIELD(Data(@"HTTP/1.0 400 Bad Request"));
            else if(code == 501)
                GENERATOR_YIELD(Data(@"HTTP/1.0 501 Not Implemented"));
            else
                GENERATOR_YIELD(Data(@"HTTP/1.0 500 Internal Server Error"));
            
            NSString *str = [NSString stringWithFormat:
                @"\r\n"
                @"Content-type: text/html\r\n"
                @"\r\n"
                @"The server generated error code %d while processing the HTTP request",
                code];
            GENERATOR_YIELD(Data(str));
        }
        GENERATOR_END
    }
```

Next, the "not found" handler simply generates a typical

error page:

```
    GENERATOR(NSData *, NotFoundHandler(NSString *resource), (void))
    {
        GENERATOR_BEGIN(void)
        {
            NSString *str = [NSString stringWithFormat:
                @"HTTP/1.0 404 Not Found\r\n"
                @"Content-type: text/html\r\n"
                @"\r\n"
                @"The resource %@ could not be found",
                HTMLEscape(resource)];
            GENERATOR_YIELD(Data(str));
        }
        GENERATOR_END
    }
```

The root handler just displays a little welcome page with a link to a more interesting handler:

```
    GENERATOR(NSData *, RootHandler(NSString *resource), (void))
    {
        GENERATOR_BEGIN(void)
        {
            NSString *str = @"HTTP/1.0 200 OK\r\n"
                            @"Content-type: text/html\r\n"
                            @"\r\n"
                            @"Welcome to GCDWeb. There isn't much here. <a href=\"listing\">Try the listing.</a>";
            GENERATOR_YIELD(Data(str));
        }
        GENERATOR_END
    }
```

Finally there's a listing handler, which serves to illustrate the asynchronous nature of this server. It just lists the full contents of

using an

. The server architecture allows the response to be generated incrementally and sent to the client as the response is created, rather than buffering it all and sending it in one big chunk, and yet the response handler code is, once again, completely straightforward top-to-bottom:

```
    GENERATOR(NSData *, ListingHandler(NSString *resource), (void))
    {
        __block NSEnumerator *enumerator = nil;
        GENERATOR_BEGIN(void)
        {
            NSString *str = @"HTTP/1.0 200 OK\r\n"
                            @"Content-type: text/html; charset=utf-8\r\n"
                            @"\r\n"
                            @"Directory listing of <tt>/tmp</tt>:<p>";
            GENERATOR_YIELD(Data(str));
            
            NSFileManager *fm = [[NSFileManager alloc] init]; // +defaultManager is not thread safe
            enumerator = [[fm enumeratorAtPath: @"/tmp"] retain];
            [fm release];
            
            NSString *file;
            while((file = [enumerator nextObject]))
            {
                GENERATOR_YIELD(Data(file));
                // note: file is no longer valid after this point!
                
                GENERATOR_YIELD(Data(@"<br>"));
            }
        }
        GENERATOR_CLEANUP
        {
            [enumerator release];
        }
        GENERATOR_END
    }
```

And that's all of the significant code in the server. There are a couple of helpers, and the code to manage the

structure, which i won't go over here, but you can always

read the source

if you want to see them.

**Conclusion**  
 The combination of GCD and generators makes for a relatively simple asynchronous server architecture. 400 lines of code gives us a fairly complete, if not very featureful, web server which is fully multithreaded to handle multiple connections simultaneously, and which automatically uses thread pools to distribute work.

However, this server is not very efficient due to reading and writing single bytes. A better technique would be to manage buffers. Doing so would not make the code too much more complex, and would eliminate a great deal of overhead. This would, I think, push this server into the realm of being reasonable to use for real-world situations.

Another interesting thing to consider is that the response side of the server is only asynchronous in one direction. Resource handlers commonly read files, but the architecture of this server does not allow for asynchronous reading of files in the resource handler, only asynchronous writing of the data. Although probably not a problem in normal situations (the file read can simply block for a bit, and it won't cause trouble except for holding on to a worker thread until it's done) it would be cleaner and potentially more efficient to make the server asynchronous in both directions.

Accomplishing this would be a fair amount of work. The write side would need to use two dispatch sources, one for the write socket and one for the file, and would have to suspend and resume them in a complicated fashion to stop GCD from calling the event handler of one source while waiting for the other source to open up. It could be done, and wouldn't be enormously complicated, but is well beyond the scope of this demonstration server.

That wraps up this week's edition. Come back in 5e-1 fortnights for a special (as in, you won't want to read it) first anniversary retrospective edition. As always, [keep your suggestions for topics coming](mailto:mike@mikeash.com). Friday Q&A is driven by your ideas, so if you'd like to see something discussed here, send it in.

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

Comments RSS feed for this page

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
