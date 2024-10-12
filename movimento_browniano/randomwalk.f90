!!
!! Samuel C. Rodrigues
!! Movimento Browniano
!! Projeto 2, PSF
!! UnB, 2022
!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

module globais
real :: t,x,dx,dt,u,q,variancia,media
integer :: tempo, amostras
real, allocatable,dimension(:,:) :: ensemble
end module globais
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
program mov_browniano
use globais
implicit none
integer :: i,j

write(*,*)'Escreva q'
read(*,*)q
dx = 1.0
dt = 3.0
!q = 0.5
tempo = 500
amostras = 1000
allocate(ensemble(amostras,tempo))

call caminhadas !simula as caminhadas e armazena os dados no array "ensemble"
open(1,file = 'media_temp.txt')
   do i=1,tempo
      media = sum(ensemble(:,i))/amostras
      write(1,*)i, media
   end do
close(1)

open(2,file = 'variancias.txt')
   do j=1,tempo
      variancia = sum(ensemble(:,j)**2)/amostras - (sum(ensemble(:,j))/amostras)**2
      write(2,*)j, variancia
   end do
close(2)

end program mov_browniano
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
subroutine caminhadas
use globais
implicit none
integer :: i,j

open(1,file = 'trajetorias.txt')
do i=1,amostras
  x = 0.0
  t = 0.0
  write(1,*)t,x
  do j=1,tempo
     call random_number(u)
     if (u .lt. q) x=x+dx
     if (u .ge. q) x=x-dx
     t=t+dt
     ensemble(i,j) = x
     write(1,*)t,x
     write(1,*)
     write(1,*)
  end do
end do
close(1)

end subroutine caminhadas
