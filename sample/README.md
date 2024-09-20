
# Spring Customizer

``` bash
export SPRING_CUSTOMIZER_ROBOT=step_floor
export SPRING_CUSTOMIZER_CONF_FILE=$(pwd)/SpringCustomizerSettings.yaml
choreonoid step_world.cnoid
```

## Arguments

- SPRING_CUSTOMIZER_ROBOT

Set robot name to affect this customizer

- SPRING_CUSTOMIZER_CONF_FILE

Yaml file, setting descriptions of spring coefficients

``` yaml
springs:
  - joint_name: <str> ## name of joint
    K: <float> ## Spring coefficient
    D: <float> ## Damping coefficient
    upper_limit: <float> ## upper_limit of joint-angle
    lower_limit: <float> ## lower_limit of joint-angle
  - joint_name: <str>
    K: <float>
    D: <float>
    upper_limit: <float>
    lower_limit: <float>
  - ...
```
