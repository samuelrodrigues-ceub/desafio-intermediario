program valordepi
implicit none
integer :: i,j,k,l, Ncir, Np, Nr,medias
real    :: u1, u2, x, x0, y, y0, lado, raio, areaC, areaMedia, pi, sigma
real, allocatable, dimension(:)  :: elementos

medias = 200
Nr = 100
Np = 100
x0 = 2.0
y0 = 3.0
raio = 1
lado = 5.0

open(unit = 3, file = 'pi_np.txt')
   do k=1,medias
      allocate(elementos(Nr))
      do j=1,Nr
         Ncir = 0
         do i=1,Np
            call random_number(u1)
            call random_number(u2)
            x = 5.0*u1
            y = 5.0*u2
 
            if ((x-x0)**2 + (y-y0)**2 .le. raio**2) then
               Ncir = Ncir + 1
               !write(1,*)x,y
            end if
            if ((x-x0)**2 + (y-y0)**2 .gt. raio**2) then
               !write(2,*)x,y
            end if
         end do
         areaC = (lado**2 *Ncir/Np)/raio**2
         elementos(j) = areaC
         !write(4,*)Np, areaC                                    !valores médios de pi em função de Np
         !Np = Np+100
      end do
      sigma = sqrt( sum(elementos**2)/Nr - (sum(elementos)/Nr)**2 )
      write(3,*)Nr, sigma                                    
      !write(4,10)raio, sum(elementos)/Nr                       !valores de pi em f do raio
      !Np = Np + 100
      Nr = Nr + 100
      !raio = raio + 0.01
      deallocate(elementos)
   end do
close(3)

10 format (f4.2,2x,f11.8)
end program valordepi
