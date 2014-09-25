package com.example.${name}.config

import com.example.${name}.collectors.CollectorConfig
import scala.reflect.BeanProperty

class ${Name}Config extends ServiceConfiguration {
  @BeanProperty var collector = new CollectorConfig
}
