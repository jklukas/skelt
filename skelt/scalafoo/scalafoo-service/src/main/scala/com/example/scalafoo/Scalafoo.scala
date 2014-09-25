package com.example.scalafoo

import com.example.scalafoo.config.ScalafooConfig
import com.example.scalafoo.db.RedshiftQueries
import com.example.jdub.DatabaseHealthCheck
import com.yammer.dropwizard.config.{Bootstrap, Environment}

object Scalafoo extends BaseService[ScalafooConfig]("scalafoo") {

  def runService(config: ScalafooConfig, env: Environment) {

    val db = DatabaseFactory.connect(config.db)

    env.addHealthCheck(new DatabaseHealthCheck(db))

  }

}
