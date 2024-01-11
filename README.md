# CubeSat_Design_Tool

This is an attempt to reverse engineer a CubeSat design tool. The following notes are specific to this process.

## Reverse Engineering Process

1. get it to work
2. document relationships
3. clean it up (OPTIONAL)
4. define models for extension
5. incrementally extend logic

## Identifying the Design

* unique application => usecase & user
* usecase => workflows
* workflows => answer questions, solve problems
* SUCCESS := application reduce pain, enable new capabilities

## Questions/Unknown

1. What is the intended "Run" / "Finish" behavior?
2. Why does it get stuck reading tabular inputs?
3. What are the defaults / are there defaults?
4. Where did development leave off?
5. What "tabs" / modules are functional? Placeholders? Not started?
6. What is the relationship / process between tabs / subsystems?
7. What is the high-level design objective / workflow / output?

## Next Steps

1. identify outputs
2. enforce single dialog for subsystem UIs
3. separate GUI/layout from subsystem modeling
4. export/capture modeling schemas
5. procedurally generate GUI and other data classes from modeling schemas

