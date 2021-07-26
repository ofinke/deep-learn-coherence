function gauss = retgauss(x, sig)
    
    x = cell2mat(x);
    gauss = exp(-(1/2)*(x./sig).^2);
    
end