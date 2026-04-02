-- Análise 1: Distribuição de documentos por tipo documental

SELECT tipo_documental, COUNT(*) AS quantidade
FROM inventario_prado_chaves_limpo
GROUP BY tipo_documental
ORDER BY quantidade DESC;


-- Análise 2: Distribuição de documentos por assunto 

SELECT assunto, COUNT(*) AS quantidade
FROM inventario_prado_chaves_limpo
GROUP BY assunto
ORDER BY quantidade DESC;


-- Análise 1: Cruzamento de tipo de assunto x tipo documental

SELECT tipo_de_assunto, tipo_documental, COUNT(*) AS quantidade
FROM inventario_prado_chaves_limpo
GROUP BY tipo_de_assunto, tipo_documental
ORDER BY tipo_de_assunto, quantidade DESC;