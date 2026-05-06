# Copilot Instructions for This Repository

## Build, test, and lint commands

This repository currently has no build, test, or lint tooling configured (no package manager manifests or test runner config are present). There is also no single-test command available at this time.

## High-level architecture

This is a document-first workspace for a professional resume, not an application codebase:

- `Resume.pdf` is the primary deliverable used for sharing the profile.
- `GEMINI.md` is the structured project context describing profile focus, experience highlights, intended usage, and planned future expansion.

Most meaningful updates are content/consistency updates across these two files rather than code changes.

## Key conventions

- Keep professional facts consistent across `Resume.pdf` and `GEMINI.md` (roles, dates, skills, projects, and education).
- Treat this repository as career-profile source material: resume maintenance and related professional-content generation are in scope.
- Do not assume software build pipelines exist here unless new tooling files are added in the future.

## Existing guidance incorporated

Important repository-specific guidance in this file is derived from `GEMINI.md`.
