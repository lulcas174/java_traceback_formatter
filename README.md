trace_java_exemplo = """
java.lang.RuntimeException: Falha ao invocar o método de negócio
    at com.framework.internal.Proxy.invoke(Proxy.java:123)
    at com.sun.proxy.$Proxy42.executarNegocio(Unknown Source)
    at com.meuapp.MeuController.handleRequest(MeuController.java:58)
    at org.springframework.web.servlet.DispatcherServlet.doDispatch(DispatcherServlet.java:1040)
    ... 45 more
Caused by: com.meuapp.repository.ErroDeBancoDeDadosException: Não foi possível acessar os dados do cliente
    at com.meuapp.repository.ClienteRepository.findById(ClienteRepository.java:99)
    at com.meuapp.MeuServico.buscarCliente(MeuServico.java:75)
    at com.meuapp.MeuServico.processar(MeuServico.java:40)
    at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
    at java.lang.reflect.Method.invoke(Method.java:498)
    ... 50 more
Caused by: java.sql.SQLTimeoutException: ORA-01013: o usuário solicitou o cancelamento da operação atual
    at oracle.jdbc.driver.T4CPreparedStatement.executeForDescribe(T4CPreparedStatement.java:876)
    at oracle.jdbc.driver.OracleStatement.executeMaybeDescribe(OracleStatement.java:1167)
    at oracle.jdbc.driver.OracleStatement.doExecuteWithTimeout(OracleStatement.java:1289)
    at oracle.jdbc.driver.OraclePreparedStatement.executeInternal(OraclePreparedStatement.java:3584)
    at oracle.jdbc.driver.OraclePreparedStatement.executeQuery(OraclePreparedStatement.java:3628)
    at com.zaxxer.hikari.pool.ProxyPreparedStatement.executeQuery(ProxyPreparedStatement.java:52)
    at com.meuapp.repository.ClienteRepository.findById(ClienteRepository.java:95)
    ... 55 more
"""
