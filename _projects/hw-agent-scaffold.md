---
layout: page
title: "Hardware starter: your first passing simulation"
description: "Generate a counter, testbench, and MCP configuration, then run a self-checking simulation."
importance: 1
category: Open-source tools
portfolio_id: hw-agent-scaffold
published: true
---

## The problem

Starting a hardware project needs consistent source files, a testbench entry point, runtime setup, and client configuration. Missing one makes even a small experiment difficult to reproduce.

## What I built

I built an npx scaffolder that creates a counter design, self-checking testbench, Makefile, and configuration for nine hardware MCP servers. It connects the tools through a concrete first project.

{% include portfolio_project.liquid %}

## A first useful result

Generate a project with `npx -y @zesun33/create-hw-agent`, then run `make sim` with Podman. The testbench checks the first increment and modulo-16 wrap. The tutorial deliberately introduces an increment bug so you can see the failure gate work.

## Evidence and limits

The starter has automated scaffold tests, and the tutorial records actual simulation execution. A passing counter test establishes the exercised functional behavior. Next, add an event-enable input or connect an MCP client; board programming and physical design are separate steps.
