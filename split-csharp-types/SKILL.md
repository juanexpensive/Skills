---
name: split-csharp-types
description: Review and refactor C# code so each class, interface, enum, struct, or record lives in its own physical file and folder structure reflects responsibility. Use when Codex needs to split mixed-type C# files, normalize namespaces to match folder structure, move enums or result records out of service files, create subfolders inside Services by domain, or relocate contracts/models/DTOs outside Services.
---

# Split Csharp Types

Refactor C# source so every named type gets its own file, support folders match responsibility, and the final result is easy to apply in a real project.

## Workflow

1. Inspect the original file or target area and list every named type declared in it.
2. Classify each type before moving it:
   `class`, `interface`, `enum`, `struct`, and `record` all count as independent types.
   Distinguish service logic, infrastructure, resolvers/helpers, DTOs, models/contracts, enums, and result objects.
3. Create one physical file per named type.
4. Choose a destination folder that matches responsibility instead of origin:
   keep behavior in service areas, move data-only types to `/Models`, `/DTOs`, `/Contracts`, or `/Common`, and use `/Enum` or `/Enums` for enums according to project convention.
5. If a service area is getting crowded, introduce subfolders inside `/Services` by responsibility or domain such as `/Services/Alerts`, `/Services/Smtp`, `/Services/Push`, or `/Services/Infrastructure`.
6. Update namespaces so they reflect the real folder structure.
7. Review access modifiers:
   use `internal` when the type is project-local and does not need to be public;
   use `public` only when external use or cross-assembly exposure is justified.
8. Remove inline helper types from the original file after moving them.
9. Update all dependent files, dependency injection registrations, and `using` directives.
10. Validate the refactor by building or running the narrowest available verification command.

## Hard Rules

- Keep exactly one named type per physical file.
- Do not leave secondary helper types in the same file as the main type, even when they are small.
- Do not keep `enum` or `record` results inline with a service or controller.
- Do not leave contracts, request/response models, result records, or DTO-like types inside `/Services` just because they were declared there originally.
- Do not treat every extracted type as a service. A file living beside a service today does not make it a service tomorrow.
- Do not create flat service directories when responsibility-based subfolders would clearly improve navigation.
- Do not describe "you should create these files" without actually showing each file separately when the user asked for the resulting files.
- Preserve behavior; only change naming, placement, namespaces, and accessibility when needed for the split.

## Placement Guidance

- Put service classes in the existing service area when the project already has one, but organize them into subfolders when there are several responsibilities.
- Put DTO-like request/response/result types in `/DTOs`, `/Contracts`, or `/Models` based on project convention; prefer not to leave them in `/Services`.
- Put domain-neutral result records and supporting response objects in `/Models` or `/Common` unless the project already has a stronger convention.
- Put infrastructure abstractions and implementations in a dedicated area such as `/Services/Infrastructure`, `/Infrastructure`, or the nearest existing equivalent.
- Put enums in `/Enum` or `/Enums` when the project has that folder; otherwise prefer `/Common` or the nearest logical shared folder.
- Mirror the project's existing naming and folder conventions before inventing new ones.
- Favor consistency over theoretical purity: follow singular vs plural folder names already present in the project.

## Service Folder Heuristics

- Group services by domain or capability when there are multiple related files:
  `/Services/Smtp`, `/Services/Alerts`, `/Services/Push`, `/Services/Auth`, `/Services/Infrastructure`.
- Keep resolvers, processors, stores, senders, hosted services, and notifiers under the service branch that matches what they do.
- If a static resolver or helper is tightly coupled to a feature workflow, it may stay under that feature's service subfolder instead of being pushed into a generic utilities folder.
- Only create a new top-level folder outside `/Services` when the type is clearly not service behavior.

## Namespace Rules

- Match the namespace to the destination folder path.
- If moving `Foo` from `MyApp.Services` to `MyApp.Services.Smtp`, update the namespace accordingly.
- If moving data types from `MyApp.Services` to `MyApp.Models`, update every consumer to import `MyApp.Models`.
- Keep `using` directives minimal after the split.
- Remove stale imports from old namespaces after the move.

## Validation

- Re-scan the affected area and confirm there is still only one named type per file.
- Build the project when practical; otherwise run the narrowest relevant verification available.
- Check for broken DI registrations or references caused by namespace moves.

## Output Format

When producing the refactor, show every required file separately.

Use this structure:

`Archivo sugerido: NombreArchivo.cs`

```csharp
// contenido completo
```

If the split requires three files, show the three files separately. Do not collapse them into one snippet.

## Review Checklist

- Did every named type get its own file?
- Do namespaces match the destination folders?
- Did enums and records stop living inside service files?
- Did contracts/models/DTO-like types move out of `/Services` when appropriate?
- Did the service area gain subfolders when a flat list was becoming noisy?
- Are access modifiers tighter where possible?
- Did dependent files and DI registrations get updated after namespace moves?
- Was the result validated with a build or equivalent check?
- Did the answer include every required file separately?
