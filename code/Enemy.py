#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import ENTITY_SPEED, ENTITY_SHOT_DELAY, WIN_HEIGHT
from code.EnemyShot import EnemyShot
from code.Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]
        #defini a direção inicial e velocidade
        self.vertical_direction = -1
        self.vertical_speed = ENTITY_SPEED[self.name]

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]

        # Lógica específica para Enemy3 no eixo Y
        if self.name == 'Enemy3':
            # Movimentar no eixo Y (subindo e descendo)
            self.rect.centery += self.vertical_speed * self.vertical_direction

            # Se atingir a borda inferior da tela, inverte a direção para subir
            if self.rect.bottom >= WIN_HEIGHT:
                self.vertical_direction = -1
                self.vertical_speed = ENTITY_SPEED[self.name]

            # Se atingir a borda superior da tela, inverte a direção para descer com o dobro da velocidade
            elif self.rect.top <= 0:
                self.vertical_direction = 1
                self.vertical_speed = 2 * ENTITY_SPEED[self.name]

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))
