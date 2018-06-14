---
published: true
layout:  post
title: "Writing a driver for a USB Multiplexer device"
display_date: 2018-04-23
categories: work
img: "https://lh3.googleusercontent.com/nV_GQhYJlNfoJGaJ5OuOio0xicyHMYhfg2p_rQHah1K7iuYAwQLEpZTC-jP6e39cFcPbAGj1awvIg602gLF2e4mLBB7vVo1qkq6OlxywRdQPNGzR4F92jYsua4WbZfbR2MePabFLIqoHEf-k5fEwAb31c5ID7YQsESizFSP6QpS3j1XxifFUS9kSFHeIbILH-Yc9mI5mejcDVMAJzrImUpuLFDRUT7IKPdR-zztH8iFvciGEY2xJ06RFp52og46Fu-oYd6O6VI0WZoPQVcH1I6fe5wE6YkG4dZpZqrbTit5btqnhX6towPyhFwMRgUcvCB8E3LENf7po-t8bqyMAE6pwkUSLzakkkzKuA1SN-i9YR5oEkRmH2E0H5YAJ6VLK0q_S3VD8_w8ue_J-y8FmmwZnlDZPV2eINOAGM7pM0f6nN7ekvXeOC_xTytPVMqa2hTWO3G0voYKUt2If-UakVnmz5WbFcxw2zIJF_Y0PE5X5KmkP8qlhOKKr4DoVqq5ALjM7vqqsvFSq1WviLbeYWC6oJXcJAHdosUfYVme7ehIv2vpLjO3JLz61DHT4HMJ9lyfN1ZKX37YgH1NzESfl50cmUqjOun69uiM3bLU=w1240-h930-no"
description: After getting used to the uiautomator tool for future tasks we were asked to write a driver for a device they needed to use for their tests.
---

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{{ page.description }}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;They had this USB Multiplexer from Cleware; it allows you to switch from USB ports(or to simulate a USB plug-in or plug-out) by the press of a button or through a computer command. Their goal was to integrate it in their test flow to automate USB plugs-in and plugs-out programmaticaly.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The manufacturer did provide some documentation as well as some piece of software in the C language to interact with the device. However the test tools that our colleagues use are written in Python and, thus, they needed a tool to control the device written in Python.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;We had the choice to either make a wrapper of the manufacturer's tool, or, better and more interesting for us to code, to develop a driver in Python that has no C code dependency. We went for the latter.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The documentation available on the manufacturer's website was not really helpful. We downloaded the code samples off their website and compiled it on our machines as we dug through the code to understand how it worked.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The tool was meant to run on linux machines; I had a virtual machine running linux Debian to work on but it wasn't really convenient to work with, especially because I wasn't sure how USB port forwarding was done between the virtual machine and the Windows host so I installed a linux operating system in dual boot with Windows 10.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;I had to do a lot of research regarding the way linux operating systems communicates with USB devices, especially with Human Interface Devices. HID are devices such as mice or keyboards that communicates with an Operating System through an USB port on the host machine. The device sends data buffers to the OS via the USB port, or the other way around, and a driver on the OS understands those raw data and act accordingly (move the cursor if we take a mouse as an example).

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;In the case of our Multiplexer, our driver had to know which USB port was turned on on the device from the data it received through the USB port; and it also had to send 
