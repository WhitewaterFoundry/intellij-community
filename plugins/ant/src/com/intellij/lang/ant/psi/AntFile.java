package com.intellij.lang.ant.psi;

import com.intellij.lang.ant.psi.introspection.AntTypeDefinition;
import org.jetbrains.annotations.NotNull;
import org.jetbrains.annotations.Nullable;

public interface AntFile extends AntElement {
  @NotNull
  AntTypeDefinition[] getBaseTypeDefinitions();

  @Nullable
  AntTypeDefinition getBaseTypeDefinition(final String taskClassName);

  @NotNull
  AntTypeDefinition getTargetDefinition();

  void registerCustomType(final AntTypeDefinition def);
}
