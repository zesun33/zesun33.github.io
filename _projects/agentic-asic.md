---
layout: page
title: "ASIC workflow orchestration"
description: "Coordinate review, verification, synthesis, and implementation through explicit MCP stages."
importance: 5
category: Open-source tools
portfolio_id: agentic-asic
published: true
---

## The problem

An RTL-to-implementation workflow involves several tools and distinct verdicts. A command succeeding at one stage can be mistaken for overall success unless inputs, failures, and artifacts are carried forward explicitly.

## What I built

I built a Python orchestrator that calls ASIC-oriented MCP tools and collects stage results into structured reports. Its tests exercise client contracts, stage behavior, and fixture flows.

{% include portfolio_project.liquid %}

## A first useful result

Read the example specification and use `asic doctor` to inspect command availability before attempting a full flow. Complete the tutorial counter review/simulation/synthesis first so the individual gates are understandable.

## Evidence and limits

Golden transcripts document example outcomes. A software gate summary is not manufacturing qualification. Physical stages need clock constraints, technology files, and fresh checks; successful orchestration does not establish a production-ready chip.
