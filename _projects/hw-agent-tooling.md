---
layout: page
title: "Hardware agent tooling: how the pieces fit"
description: "Follow the tool family from runtime and review guidance to simulation, synthesis, and workflow automation."
importance: 6
category: Open-source tools
portfolio_id: hw-agent-tooling
published: true
---

## The problem

Hardware tooling spans containers, editor environments, review rubrics, individual operations, CI, and orchestration. A collection of repository names does not explain which piece to use first.

## What I built

I organized EDA MCP servers, agent instruction packs, runtime images, a starter CLI, and workflow tools. This hub explains their relationships and includes a FIFO review → simulation → synthesis walkthrough.

{% include portfolio_project.liquid %}

## A first useful result

Start with the scaffold for a first simulation, use one MCP server for a specific operation, or read the FIFO walkthrough. The tutorial adds smaller consecutive exercises and a real MCP SDK client that needs no LLM account.

## Evidence and limits

Each tool keeps its own code, checks, and releases. The hub transcripts illustrate a workflow; fresh execution and toolchain versions establish a result for your input. The complete directory distinguishes usable tools from exercises and architecture plans.
