---
title: OpenGL Queries
apple_id: TP40016611
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/OpenGL_Queries/Listings/Sources_Frameworks_Model_Foundation_Query_Hardware_Core_CFQueryHardware_mm.html
archived_at: '2026-07-18T03:18:12.975720Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OpenGL Queries](OpenGL%20Queries.md)


[Next](Sources-Frameworks-Model-Foundation-Query-Hardware-Core-CFQueryHardware.h.md)[Previous](Sources-Frameworks-View-AppDelegate.mm.md)

# Sources/Frameworks/Model/Foundation/Query/Hardware/Core/CFQueryHardware.mm

```objc
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Utility class for querying hardware features.
 */

#pragma mark -
#pragma mark Private - Headers

#import <cstdio>
#import <cstdlib>

#import <sys/types.h>
#import <sys/sysctl.h>

#import "CFQueryHardware.h"

#pragma mark -
#pragma mark Public - Constants

double_t CF::Query::Frequency::kGigaHetrz = 1.0e-9;
double_t CF::Query::Frequency::kMegaHertz = 1.0e-6;
double_t CF::Query::Frequency::kKiloHertz = 1.0e-3;
double_t CF::Query::Frequency::kHertz     = 1.0f;

#pragma mark -
#pragma mark Private - Constants

static const size_t kGigaBytes = 1073741824;

#pragma mark -
#pragma mark Private - Utilities

static int CFQueryHardwareGetMemSize(size_t& gigabytes)
{
    size_t size  = sizeof(size_t);
    size_t bytes = sizeof(size_t);

    int result = sysctlbyname("hw.memsize", &bytes, &size, nullptr, 0);

    if(result < 0)
    {
        std::perror("sysctlbyname() failed for memory size!");
    } // if
    else
    {
        gigabytes = bytes / kGigaBytes;
    } // else

    return result;
} // CFQueryHardwareGetMemSize

static int CFQueryHardwareGetCPUCount(size_t& count)
{
    size_t size = sizeof(size_t);

    int result = sysctlbyname("hw.physicalcpu_max", &count, &size, nullptr, 0);

    if(result < 0)
    {
        std::perror("sysctlbyname() failed for max physical cpu count!");
    } // if

    return result;
} // CFQueryHardwareGetCPUCount

static int CFQueryHardwareGetCPUFreq(const double_t& scale,
                                     double_t& fCPU)
{
    size_t freq = 0;
    size_t size = sizeof(size_t);

    int result = sysctlbyname("hw.cpufrequency_max", &freq, &size, nullptr, 0);

    if(result < 0)
    {
        std::perror("sysctlbyname() failed for cpu frequency!");
    } // if
    else
    {
        fCPU = double_t(freq) * scale;
    } // else

    return result;
} // CFQueryHardwareGetCPUFreq

static int CFQueryHardwareGetModel(std::string& model)
{
    size_t nLength = 0;

    int result = sysctlbyname("hw.model", nullptr, &nLength, nullptr, 0);

    if(result < 0)
    {
        std::perror("sysctlbyname() failed in acquring string length for the hardware model!");

        return result;
    } // if

    if(nLength)
    {
        char* pModel = new (std::nothrow) char[nLength];

        if(pModel != nullptr)
        {
            int result = sysctlbyname("hw.model", pModel, &nLength, nullptr, 0);

            if(result < 0)
            {
                std::perror("sysctlbyname() failed in acquring a hardware model name!");
            } // if
            else
            {
                model = pModel;
            } // else

            delete [] pModel;

            pModel = nullptr;
        } // if
        else
        {
            std::perror("sysctlbyname() failed in acquring a string buffer for the hardware model!");

            result = -1;
        } // catch
    } // if

    return result;
} // CFQueryHardwareGetModel

#pragma mark -
#pragma mark Public - Hardware

CF::Query::Hardware::Hardware(const double_t& frequency)
{
    mnCores = 0;
    mnCPU   = 0.0f;

    mnFreq = (frequency > 0.0f) ? frequency : CF::Query::Frequency::kGigaHetrz;

    CFQueryHardwareGetCPUCount(mnCores);
    CFQueryHardwareGetMemSize(mnSize);
    CFQueryHardwareGetModel(m_Model);

    CFQueryHardwareGetCPUFreq(mnFreq, mnCPU);
} // Constructor

CF::Query::Hardware::~Hardware()
{
    mnCores = 0;
    mnSize  = 0;
    mnCPU   = 0.0f;
    mnFreq  = 0.0f;

    m_Model.clear();
} // Destructor

CF::Query::Hardware::Hardware(const CF::Query::Hardware& hw)
{
    mnCores = hw.mnCores;
    mnSize  = hw.mnSize;
    mnCPU   = hw.mnCPU;
    mnFreq  = hw.mnFreq;
    m_Model = hw.m_Model;
} // Copy Constructor

CF::Query::Hardware& CF::Query::Hardware::operator=(const CF::Query::Hardware& hw)
{
    if(this != &hw)
    {
        mnCores = hw.mnCores;
        mnSize  = hw.mnSize;
        mnCPU   = hw.mnCPU;
        mnFreq  = hw.mnFreq;
        m_Model = hw.m_Model;
    } // if

    return *this;
} // operator=

const size_t& CF::Query::Hardware::cores() const
{
    return mnCores;
} // cores

const size_t& CF::Query::Hardware::memory() const
{
    return mnSize;
} // memory

const double_t& CF::Query::Hardware::cpu() const
{
    return mnCPU;
} // cpu

const std::string& CF::Query::Hardware::model() const
{
    return m_Model;
} // model
```

[Next](Sources-Frameworks-Model-Foundation-Query-Hardware-Core-CFQueryHardware.h.md)[Previous](Sources-Frameworks-View-AppDelegate.mm.md)

