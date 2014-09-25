package com.example.${name}

import com.example.${name}.config.${Name}Config
import com.example.${name}.db.RedshiftQueries
import com.example.jdub.DatabaseHealthCheck
import com.yammer.dropwizard.config.{Bootstrap, Environment}

object ${Name} extends BaseService[${Name}Config]("${name}") {

  def runService(config: ${Name}Config, env: Environment) {

    val db = DatabaseFactory.connect(config.db)

    env.addHealthCheck(new DatabaseHealthCheck(db))

  }

}
