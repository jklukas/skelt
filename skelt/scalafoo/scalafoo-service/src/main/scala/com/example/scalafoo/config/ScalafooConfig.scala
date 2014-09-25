package com.example.scalafoo.config

import com.example.scalafoo.collectors.CollectorConfig
import scala.reflect.BeanProperty

class ScalafooConfig extends ServiceConfiguration {
  @BeanProperty var collector = new CollectorConfig
}
